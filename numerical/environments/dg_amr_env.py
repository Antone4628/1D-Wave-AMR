"""
This environment implements reinforcement learning-based adaptive mesh refinement 
for discontinuous Galerkin methods.

The environment provides:
- Observation space based on solution jumps and resource usage
- Action space for element refinement decisions
- Reward function balancing accuracy and computational cost
"""

import gymnasium as gym
import numpy as np
from gymnasium import spaces
from time import time
from typing import Optional, Dict, Tuple, Any
import matplotlib.pyplot as plt
from ..solvers.dg_wave_solver_clean import DGWaveSolver


class RewardCalculator:
    """
    Handles reward calculation for the AMR environment.
    """
    def __init__(self, gamma_c=25.0, machine_eps=1e-16):
        self.gamma_c = gamma_c
        self.machine_eps = machine_eps

    def calculate_barrier(self, resources):
        """Calculate barrier function B(p)"""
        if resources >= 1.0:
            return float('inf')  # Or a very large value
        elif resources <= 0.0:
            return 0.0
        else:
            return np.sqrt(resources) / (1 - resources)  # Non-hortative barrier function
        
    def calculate_resource_penalty(self, resource_usage):
        """Calculate penalty for resource usage with progressive scaling"""
        if resource_usage < 0.7:  # Plenty of resources
            return self.gamma_c * 0.1 * resource_usage  # Very small penalty
        elif resource_usage < 0.9:  # Getting closer
            return self.gamma_c * (0.1 * 0.7 + 0.5 * (resource_usage - 0.7))  # Moderate penalty
        else:  # Very close to budget
            base_penalty = self.gamma_c * (0.1 * 0.7 + 0.5 * 0.2)  # Previous ranges
            return base_penalty + self.gamma_c * 2.0 * (resource_usage - 0.9)  # Sharp increase
        

    def calculate_reward(self, delta_u: float, action: int, old_resources: float, new_resources: float) -> float:
        """
        Compute reward with progressive penalties
        """
        # Base accuracy term (before applying sign)
        accuracy_term = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
        # Apply sign based on action (equation 5)
        if action == 1:  # refine
            accuracy = +accuracy_term
        elif action == -1:  # coarsen
            accuracy = -accuracy_term
        else:  # do nothing
            accuracy = 0.0
        
        # Resource penalty using progressive function
        old_penalty = self.calculate_resource_penalty(old_resources)
        new_penalty = self.calculate_resource_penalty(new_resources)
        resource_penalty = new_penalty - old_penalty
        
        return float(accuracy - resource_penalty)


    # def calculate_resource_penalty(self, new_resources):
    #     """Calculate penalty for resource usage"""
    #     if new_resources >= 1.0:
    #         return 1000.0
    #     elif new_resources <= 0.0:
    #         return 0.0
    #     else:
    #         return self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)
        
    # def calculate_reward(self, delta_u: float, action: int, old_resources: float, new_resources: float) -> float:
    #     """
    #     Compute reward following paper's formulation.
        
    #     Args:
    #         delta_u: Change in solution after adaptation
    #         action: The action taken (-1: coarsen, 0: do nothing, 1: refine)
    #         old_resources: Previous resource usage fraction
    #         new_resources: New resource usage fraction
            
    #     Returns:
    #         float: Computed reward value
    #     """
    #     # Base accuracy term (before applying sign)
    #     accuracy_term = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
    #     # Apply sign based on action (equation 5)
    #     if action == 1:  # refine
    #         accuracy = +accuracy_term
    #     elif action == -1:  # coarsen
    #         accuracy = -accuracy_term
    #     else:  # do nothing
    #         accuracy = 0.0
        
    #     # Resource penalty using barrier function difference (equation 4)
    #     old_barrier = self.calculate_barrier(old_resources)
    #     new_barrier = self.calculate_barrier(new_resources)
    #     resource_penalty = new_barrier - old_barrier
        
    #     return float(accuracy - self.gamma_c * resource_penalty)

# def calculate_delta_u(old_solution, new_solution, old_grid, new_grid):
#     # Interpolate the solution with fewer points onto the grid with more points
#     if len(new_solution) >= len(old_solution):
#         old_interpolated = np.interp(new_grid, old_grid, old_solution)
#         # Calculate absolute differences and approximate integral
#         delta_u = np.sum(np.abs(new_solution - old_interpolated) * np.diff(np.append(new_grid, new_grid[-1])))
#     else:
#         new_interpolated = np.interp(old_grid, new_grid, new_solution)
#         delta_u = np.sum(np.abs(new_interpolated - old_solution) * np.diff(np.append(old_grid, old_grid[-1])))
#     return delta_u

def calculate_delta_u(old_solution, new_solution, old_grid, new_grid):
        """
        Calculate the L1 norm of the difference between solutions according to equation 3.
        
        Args:
            old_solution: Solution before adaptation
            new_solution: Solution after adaptation
            old_grid: Grid coordinates before adaptation
            new_grid: Grid coordinates after adaptation
            
        Returns:
            float: The integral of absolute difference between solutions
        """
        # Interpolate the solution with fewer points onto the grid with more points
        if len(new_solution) >= len(old_solution):
            old_interpolated = np.interp(new_grid, old_grid, old_solution)
            # Calculate element-wise differences
            point_differences = np.abs(new_solution - old_interpolated)
            # Calculate approximate element widths for integration
            element_widths = np.diff(np.append(new_grid, new_grid[-1] + (new_grid[-1] - new_grid[-2])))
            # Approximate the integral using element widths
            delta_u = np.sum(point_differences * element_widths)
        else:
            new_interpolated = np.interp(old_grid, new_grid, new_solution)
            point_differences = np.abs(new_interpolated - old_solution)
            element_widths = np.diff(np.append(old_grid, old_grid[-1] + (old_grid[-1] - old_grid[-2])))
            delta_u = np.sum(point_differences * element_widths)
            
        return delta_u

class DGAMREnv(gym.Env):
    """
    Custom Environment for DG Wave AMR that follows Gymnasium interface.
    
    This environment allows an RL agent to make local mesh refinement decisions
    based on solution jumps and computational resources. Each step involves:
    1. Observing the current element's state (jumps, solution values)
    2. Choosing an action (refine, coarsen, or do nothing)
    3. Receiving a reward based on solution accuracy and resource usage
    """
    
    def __init__(
        self,
        solver: DGWaveSolver,
        element_budget: int,
        gamma_c: float = 25.0,
        render_mode: str = None,
        max_episode_steps: int = 200,
        verbose: bool = False,
        rl_iterations_per_timestep = "random",
        max_rl_iterations = 200,
        debug_training_cycle=False
    ):
        """
        Initialize DG AMR environment with explicit element budget.

        Args:
            solver: Instance of DG wave solver
            element_budget: Maximum number of elements allowed
            gamma_c: Coefficient for resource penalty term in reward
            render_mode: Mode for visualization (if needed)
            max_episode_steps: Maximum steps per episode
            verbose: Whether to print detailed logs
        """
        super().__init__()
        self.solver = solver
        self.element_budget = element_budget
        self.gamma_c = gamma_c
        self.render_mode = render_mode
        self.current_element_index = 0
        self.machine_eps = 1e-16
        self.max_episode_steps = max_episode_steps
        self.episode_callback = None
        self.verbose = verbose

        # Initialize step counters
        self.num_timesteps = 0
        self._episode_steps = 0
        self._total_episodes = 0

        # Initialize reward calculator
        self.reward_calculator = RewardCalculator(gamma_c=gamma_c)
        
        # Define action space as {0, 1, 2} mapping to {-1, 0, 1}
        # -1: coarsen, 0: do nothing, 1: refine
        self.action_space = spaces.Discrete(3)
        self.action_mapping = {
            0: -1,  # coarsen
            1: 0,   # do nothing
            2: 1    # refine
        }

        # Add new parameters
        self.rl_iterations_per_timestep = rl_iterations_per_timestep  # Can be "random" or an integer
        self.max_rl_iterations = max_rl_iterations
        self.current_rl_iteration = 0
        self.should_timestep = False
        self.debug_training_cycle = debug_training_cycle  # Store the debug flag
        
        # Define observation space components
        self.observation_space = spaces.Dict({
            'avg_local_jump': spaces.Box(
                low=0.0,
                high=1e3,
                shape=(1,),
                dtype=np.float32
            ),
            'avg_jump': spaces.Box(
                low=0.0,
                high=1e3,
                shape=(1,),
                dtype=np.float32
            ),
            'jump_ratio': spaces.Box(
                low=0.0,
                high=10.0,  # Can be adjusted based on your problem
                shape=(1,),
                dtype=np.float32
            ),
            'resource_usage': spaces.Box(
                low=0.0,
                high=1.0,
                shape=(1,),
                dtype=np.float32
            ),
            # Add new budget proximity features
            'budget_proximity': spaces.Box(
                low=0.0,
                high=1.0,
                shape=(1,),
                dtype=np.float32
            ),
            'budget_headroom': spaces.Box(
                low=0, 
                high=self.element_budget,
                shape=(1,),
                dtype=np.float32
            ),
            'refinement_safety': spaces.Box(
                low=0.0,
                high=1.0,
                shape=(1,),
                dtype=np.float32
            ),
            # Keep solution_values for continuity
            'solution_values': spaces.Box(
                low=-1e3,
                high=1e3,
                shape=(self.solver.ngl,),
                dtype=np.float32
            )
        })
        
        # Add an action name dictionary for logging
        self.action_names = {-1: "Coarsen", 0: "No Change", 1: "Refine"}

        # self.observation_space = spaces.Dict({
        #     'avg_local_jump': spaces.Box(
        #         low=0.0,
        #         high=1e3,
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     'avg_jump': spaces.Box(
        #         low=0.0,
        #         high=1e3,
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     'jump_ratio': spaces.Box(
        #         low=0.0,
        #         high=10.0,  # Can be adjusted based on your problem
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     'resource_usage': spaces.Box(
        #         low=0.0,
        #         high=1.0,
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     # Keep solution_values if you need them, but consider removing for simplicity
        #     'solution_values': spaces.Box(
        #         low=-1e3,
        #         high=1e3,
        #         shape=(self.solver.ngl,),
        #         dtype=np.float32
        #     )
        # })
        # self.observation_space = spaces.Dict({
        #     'local_jumps': spaces.Box(
        #         low=0.0,
        #         high=1e3,
        #         shape=(self.solver.ngl,), 
        #         dtype=np.float32
        #     ),
        #     'neighbor_jumps': spaces.Box(
        #         low=0.0,
        #         high=1e3,
        #         shape=(2,),
        #         dtype=np.float32
        #     ),
        #     'avg_jump': spaces.Box(
        #         low=0.0,
        #         high=1e3,
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     'resource_usage': spaces.Box(
        #         low=0.0,
        #         high=1.0,
        #         shape=(1,),
        #         dtype=np.float32
        #     ),
        #     'solution_values': spaces.Box(
        #         low=-1e3,
        #         high=1e3,
        #         shape=(self.solver.ngl,),
        #         dtype=np.float32
        #     )
        # })

    def register_callback(self, callback):
        """Register a callback to be called when episodes end."""
        self.episode_callback = callback
        if self.verbose:
            print(f"Environment registered episode callback: {callback.__class__.__name__}")

    

    def _get_element_jumps(self, element_idx: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute solution jumps at element boundaries and interior nodes.
        
        Args:
            element_idx: Index of element in active_grid
                
        Returns:
            tuple: (local_jumps, neighbor_jumps)
        """
        # Safety check for valid element index
        if element_idx >= len(self.solver.active):
            if self.verbose:
                print(f"Warning: Invalid element index {element_idx}, active elements: {len(self.solver.active)}")
            return np.zeros(self.solver.ngl), np.zeros(2)
            
        # Get element number from active grid
        elem = self.solver.active[element_idx]
        
        # Extract solution values for current element
        elem_nodes = self.solver.intma[:, element_idx]
        elem_sol = self.solver.q[elem_nodes]
        
        # Get boundary values
        elem_left = elem_sol[0]
        elem_right = elem_sol[-1]
        
        # Initialize arrays for jumps
        local_jumps = np.zeros(self.solver.ngl)
        neighbor_jumps = np.zeros(2)
        
        try:
            # Handle Left Neighbor (with periodicity)
            if elem > 1:
                left_active_idx = np.where(self.solver.active == elem-1)[0]
            else:
                left_active_idx = np.where(self.solver.active == len(self.solver.label_mat))[0]
                
            if len(left_active_idx) > 0:
                left_idx = left_active_idx[0]
                left_nodes = self.solver.intma[:, left_idx]
                left_sol = self.solver.q[left_nodes]
                
                # Calculate jump at left interface
                local_jumps[0] = abs(elem_left - left_sol[-1])
                neighbor_jumps[0] = local_jumps[0]
                        
            # Handle Right Neighbor (with periodicity)
            if elem < len(self.solver.label_mat):
                right_active_idx = np.where(self.solver.active == elem+1)[0]
            else:
                right_active_idx = np.where(self.solver.active == 1)[0]
                
            if len(right_active_idx) > 0:
                right_idx = right_active_idx[0]
                right_nodes = self.solver.intma[:, right_idx]
                right_sol = self.solver.q[right_nodes]
                
                # Calculate jump at right interface
                local_jumps[-1] = abs(elem_right - right_sol[0])
                neighbor_jumps[1] = local_jumps[-1]
                        
            # Calculate Interior Jumps
            for i in range(1, self.solver.ngl-1):
                local_jumps[i] = abs(elem_sol[i] - elem_sol[i-1])
                    
        except Exception as e:
            if self.verbose:
                print(f"Error in _get_element_jumps: {e}")
                import traceback
                traceback.print_exc()
            return np.zeros(self.solver.ngl), np.zeros(2)
                
        return local_jumps, neighbor_jumps
    
    # def _get_observation(self) -> Dict[str, np.ndarray]:
    #     """
    #     Get current observation of the environment state.
        
    #     Returns:
    #         dict: Observation space components
    #     """
    #     # Get local solution jumps
    #     local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element_index)

    #     # Compute average jump across all elements
    #     all_jumps = []
    #     for i in range(len(self.solver.active)):
    #         jumps, _ = self._get_element_jumps(i)
    #         if not np.any(np.isnan(jumps)):
    #             all_jumps.append(jumps.mean())
    
    #     avg_jump = np.mean(all_jumps) if all_jumps else 0.0

    #     # Safety check for NaN values
    #     local_jumps = np.nan_to_num(local_jumps, 0.0)
    #     neighbor_jumps = np.nan_to_num(neighbor_jumps, 0.0)
        
    #     # Current resource usage
    #     resource_usage = len(self.solver.active) / self.element_budget

    #     # Get local solution values
    #     element_nodes = self.solver.intma[:, self.current_element_index]
    #     solution_values = self.solver.q[element_nodes]
    
    #     return {
    #         'local_jumps': local_jumps.astype(np.float32),
    #         'neighbor_jumps': neighbor_jumps.astype(np.float32),
    #         'avg_jump': np.array([avg_jump], dtype=np.float32),
    #         'resource_usage': np.array([resource_usage], dtype=np.float32),
    #         'solution_values': solution_values.astype(np.float32)
    #     }
    def _get_observation(self) -> Dict[str, np.ndarray]:
        """
        Get current observation with enhanced budget proximity features.
        
        Returns:
            dict: Observation space components
        """
        # Get existing features
        local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element_index)
        
        # Calculate average of local jumps for this element
        avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        
        # Compute average jump across all elements
        all_jumps = []
        for i in range(len(self.solver.active)):
            jumps, _ = self._get_element_jumps(i)
            if not np.any(np.isnan(jumps)):
                all_jumps.append(np.mean(jumps))
        
        avg_jump = np.mean(all_jumps) if all_jumps else 0.0
        
        # Calculate jump ratio (how this element compares to global average)
        epsilon = 1e-10
        jump_ratio = avg_local_jump / (avg_jump + epsilon) if avg_jump > 0 else 1.0
        jump_ratio = min(jump_ratio, 10.0)  # Cap at 10.0
        
        # Current resource usage
        current_elements = len(self.solver.active)
        resource_usage = current_elements / self.element_budget
        
        # Get local solution values
        element_nodes = self.solver.intma[:, self.current_element_index]
        solution_values = self.solver.q[element_nodes]
        
        # New budget proximity features
        budget_proximity = resource_usage  # Raw proximity (0.0 to 1.0)
        budget_headroom = self.element_budget - current_elements  # Absolute headroom
        
        # Refinement safety - probability of staying under budget if we refine
        # This depends on how many elements might be created due to balance constraints
        # Simple heuristic: 1.0 if plenty of headroom, 0.0 if at/over budget
        safe_headroom_threshold = 5  # Arbitrary threshold - adjust based on problem
        refinement_safety = min(1.0, max(0.0, budget_headroom / safe_headroom_threshold))
        
        return {
            'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'jump_ratio': np.array([jump_ratio], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'budget_proximity': np.array([budget_proximity], dtype=np.float32),
            'budget_headroom': np.array([budget_headroom], dtype=np.float32),
            'refinement_safety': np.array([refinement_safety], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }
    # def _get_observation(self) -> Dict[str, np.ndarray]:
    #     """
    #     Get current observation of the environment state with simplified features.
        
    #     Returns:
    #         dict: Observation space components
    #     """
    #     # Get local solution jumps
    #     local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element_index)
        
    #     # Calculate average of local jumps for this element
    #     avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        
    #     # Compute average jump across all elements
    #     all_jumps = []
    #     for i in range(len(self.solver.active)):
    #         jumps, _ = self._get_element_jumps(i)
    #         if not np.any(np.isnan(jumps)):
    #             all_jumps.append(np.mean(jumps))
        
    #     avg_jump = np.mean(all_jumps) if all_jumps else 0.0
        
    #     # Calculate jump ratio (how this element compares to global average)
    #     # Avoid division by zero by adding a small epsilon
    #     epsilon = 1e-10
    #     jump_ratio = avg_local_jump / (avg_jump + epsilon) if avg_jump > 0 else 1.0
        
    #     # Safety check to keep ratio in reasonable bounds
    #     jump_ratio = min(jump_ratio, 10.0)
        
    #     # Current resource usage
    #     resource_usage = len(self.solver.active) / self.element_budget
        
    #     # Get local solution values
    #     element_nodes = self.solver.intma[:, self.current_element_index]
    #     solution_values = self.solver.q[element_nodes]
        
    #     return {
    #         'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
    #         'avg_jump': np.array([avg_jump], dtype=np.float32),
    #         'jump_ratio': np.array([jump_ratio], dtype=np.float32),
    #         'resource_usage': np.array([resource_usage], dtype=np.float32),
    #         'solution_values': solution_values.astype(np.float32)
    #     }

    # def _end_episode(self, reward, terminated, truncated, reason=""):
    #     """Helper method to handle episode ending logic"""
    #     observation = self._get_observation()
        
    #     info = {
    #         'episode_steps': self._episode_steps,
    #         'total_steps': self.num_timesteps,
    #         'reason': reason,
    #         'episode': {
    #             'r': float(reward),
    #             'l': int(max(1, self._episode_steps))
    #         }
    #     }
        
    #     if self.verbose:
    #         print(f"Episode ending: {reason}")
    #         print(f"Episode reward: {reward:.2f}, length: {self._episode_steps}")

    #     # Call callback if registered
    #     if self.episode_callback is not None:
    #         self.episode_callback(reward, self._episode_steps)
            
    #     self._total_episodes += 1
    #     return observation, reward, terminated, truncated, info

    # def _end_episode(self, reward, terminated, truncated, reason=""):
    #     """Helper method to handle episode ending logic with enhanced logging"""
    #     observation = self._get_observation()
        
    #     # Track termination reasons for analysis
    #     if not hasattr(self, 'termination_stats'):
    #         self.termination_stats = {
    #             'budget_exceeded': 0,
    #             'max_steps_reached': 0,
    #             'other': 0
    #         }
        
    #     # Update termination statistics
    #     if reason == "Budget exceeded":
    #         self.termination_stats['budget_exceeded'] += 1
    #     elif reason == "Maximum episode steps reached":
    #         self.termination_stats['max_steps_reached'] += 1
    #     else:
    #         self.termination_stats['other'] += 1
        
    #     # Calculate and log termination percentages
    #     total_episodes = sum(self.termination_stats.values())
    #     if total_episodes % 10 == 0:  # Log every 10 episodes
    #         budget_pct = self.termination_stats['budget_exceeded'] / total_episodes * 100
    #         steps_pct = self.termination_stats['max_steps_reached'] / total_episodes * 100
    #         other_pct = self.termination_stats['other'] / total_episodes * 100
    #         print(f"Episode termination statistics after {total_episodes} episodes:")
    #         print(f"  Budget exceeded: {budget_pct:.1f}%")
    #         print(f"  Max steps reached: {steps_pct:.1f}%")
    #         print(f"  Other reasons: {other_pct:.1f}%")
        
    #     info = {
    #         'episode_steps': self._episode_steps,
    #         'total_steps': self.num_timesteps,
    #         'reason': reason,
    #         'episode': {
    #             'r': float(reward),
    #             'l': int(max(1, self._episode_steps)),
    #             'termination_reason': reason
    #         }
    #     }
        
    #     if self.verbose:
    #         print(f"Episode ending: {reason}")
    #         print(f"Episode reward: {reward:.2f}, length: {self._episode_steps}")

    #     # Call callback if registered
    #     if self.episode_callback is not None:
    #         self.episode_callback(reward, self._episode_steps)
            
    #     self._total_episodes += 1
    #     return observation, reward, terminated, truncated, info

    def _is_refinement_safe(self, element_idx: int) -> bool:
        """
        Check if refining an element is likely to stay within budget constraints.
        
        Args:
            element_idx: Index of element in active_grid
            
        Returns:
            bool: True if refinement is likely safe, False otherwise
        """
        current_elements = len(self.solver.active)
        
        # If already at or near budget, refinement is unsafe
        if current_elements >= self.element_budget - 1:
            return False
        
        # Get element and check if it can be refined (has no children yet)
        element = self.solver.active[element_idx]
        element_data = self.solver.label_mat[element-1]
        children = element_data[2:4]
        
        # If element already has children, it can't be refined
        if children[0] != 0:
            return False
        
        # Simple estimation of balance cascading effects 
        # In a highly imbalanced mesh, refinement might trigger multiple balance refinements
        # This is a simplified heuristic - real balance enforcement is complex
        current_level = element_data[4]  # Get element level
        
        # Get neighbor levels
        neighbor_levels = []
        if element_idx > 0:
            left_elem = self.solver.active[element_idx-1]
            left_level = self.solver.label_mat[left_elem-1][4]
            neighbor_levels.append(left_level)
        
        if element_idx < len(self.solver.active) - 1:
            right_elem = self.solver.active[element_idx+1]
            right_level = self.solver.label_mat[right_elem-1][4]
            neighbor_levels.append(right_level)
        
        # Estimate potential balance refinements
        potential_new_elements = 1  # Start with 1 for the direct refinement
        for level in neighbor_levels:
            level_diff = current_level + 1 - level
            if level_diff > 1:
                # This neighbor would need refinement for balance
                potential_new_elements += 1
        
        # Check if budget can accommodate all potential new elements
        return current_elements + potential_new_elements <= self.element_budget

    def _end_episode(self, reward, terminated, truncated, reason="", pre_term_info=None):
        """Helper method to handle episode ending logic with enhanced logging"""
        observation = self._get_observation()
        
        # Track termination reasons for analysis
        if not hasattr(self, 'termination_stats'):
            self.termination_stats = {
                'budget_exceeded': 0,
                'max_steps_reached': 0,
                'other': 0
            }
        
        # Update termination statistics
        if reason == "Budget exceeded":
            self.termination_stats['budget_exceeded'] += 1
        elif reason == "Maximum episode steps reached":
            self.termination_stats['max_steps_reached'] += 1
        else:
            self.termination_stats['other'] += 1
        
        # Calculate and log termination percentages
        total_episodes = sum(self.termination_stats.values())
        if total_episodes % 10 == 0:  # Log every 10 episodes
            budget_pct = self.termination_stats['budget_exceeded'] / total_episodes * 100
            steps_pct = self.termination_stats['max_steps_reached'] / total_episodes * 100
            other_pct = self.termination_stats['other'] / total_episodes * 100
            print(f"Episode termination statistics after {total_episodes} episodes:")
            print(f"  Budget exceeded: {budget_pct:.1f}%")
            print(f"  Max steps reached: {steps_pct:.1f}%")
            print(f"  Other reasons: {other_pct:.1f}%")
        
        info = {
            'episode_steps': self._episode_steps,
            'total_steps': self.num_timesteps,
            'reason': reason,
            'episode': {
                'r': float(reward),
                'l': int(max(1, self._episode_steps)),
                'termination_reason': reason
            }
        }
        
        # Add pre-termination metrics if available
        if pre_term_info is not None:
            for key, value in pre_term_info.items():
                info[key] = value
        
        if self.verbose:
            print(f"Episode ending: {reason}")
            print(f"Episode reward: {reward:.2f}, length: {self._episode_steps}")
            
            # Print pre-termination info if available
            if pre_term_info is not None and reason == "Budget exceeded":
                print(f"  Pre-termination elements: {pre_term_info.get('pre_termination_elements', 'N/A')}")
                print(f"  Budget usage: {pre_term_info.get('budget_usage_percent', 'N/A'):.1f}%")
                print(f"  Violation action: {pre_term_info.get('violation_action', 'N/A')}")

        # Call callback if registered
        if self.episode_callback is not None:
            self.episode_callback(reward, self._episode_steps)
            
        self._total_episodes += 1
        return observation, reward, terminated, truncated, info
    
    def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
        """
        Execute one step of the environment.
        """
        self.num_timesteps += 1
        self._episode_steps += 1
        
        # Map action and handle budget checks as you do currently
        action_int = action.item() if hasattr(action, 'item') else int(action)
        mapped_action = self.action_mapping[action_int]
        current_element = self.solver.active[self.current_element_index]

            # Add budget awareness for refinement - penalize unsafe refinements
        if mapped_action == 1:  # Refine
            refinement_safe = self._is_refinement_safe(self.current_element_index)
            
            # If refinement would exceed budget, apply a penalty and change to no-op
            if not refinement_safe:
                if self.debug_training_cycle:
                    print(f"Unsafe refinement detected. Elements: {len(self.solver.active)}/{self.element_budget}")
                
                # Option 1: Change action to no-op to prevent budget violation
                # mapped_action = 0  # No change
                
                # Option 2: Keep action but add penalty to the reward later
                unsafe_refinement = True
            else:
                unsafe_refinement = False
        else:
            unsafe_refinement = False
        
        # Check budget and episode length constraints
        # if len(self.solver.active) >= self.element_budget:
        #     return self._end_episode(-1000.0, False, True, "Budget exceeded")


        pre_action_elements = len(self.solver.active)
        # print(f"PRE-ACTION: {mapped_action} | Elements: {pre_action_elements}")


        if len(self.solver.active) >= self.element_budget:
            # Log detailed information about the budget violation
            element_count = len(self.solver.active)
            budget_usage_percent = (element_count / self.element_budget) * 100
            
            if self.verbose or self.debug_training_cycle:
                print(f"\n===== BUDGET EXCEEDED =====")
                print(f"Current elements: {element_count}/{self.element_budget} ({budget_usage_percent:.1f}%)")
                print(f"Action that triggered violation: {mapped_action} ({self.action_names[mapped_action]})")
                print(f"Element being processed: {current_element}")
                print(f"Current step in episode: {self._episode_steps}")
                
                # Log last few actions to see what led to the violation
                recent_actions = self.mapped_action_history[-min(10, len(self.mapped_action_history)):]
                recent_action_names = [self.action_names[a] for a in recent_actions]
                print(f"Recent actions: {recent_action_names}")
                print("===========================\n")
            
            # Store pre-termination metrics
            info = {
                'pre_termination_elements': element_count,
                'budget_usage_percent': budget_usage_percent,
                'violation_action': mapped_action,
                'episode_steps': self._episode_steps
            }
            
            return self._end_episode(-1000.0, False, True, "Budget exceeded", info)
        
        if self._episode_steps >= self.max_episode_steps:
            return self._end_episode(0.0, False, True, "Maximum episode steps reached", None)
        
        # Store current state for reward calculation
        old_solution = self.solver.q.copy()
        old_grid = self.solver.coord.copy()
        old_active_elements = self.solver.active.copy()  # Track elements before adaptation
        old_resources = len(self.solver.active) / self.solver.max_elements
        
        try:
            # Apply adaptation
            if self.debug_training_cycle:
                print(f"Applying adaptation for element {current_element} with action {mapped_action}")
                print(f"pre adapt active: {self.solver.active}")
            marks_override = {self.current_element_index: mapped_action}
            self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)


            # After applying the action but before checking budget:
            post_action_elements = len(self.solver.active)
            # print(f"POST-ACTION: {mapped_action} | Elements: {post_action_elements} | Change: {post_action_elements - pre_action_elements}")
            
            # Add this after the post-action print statement
            if len(self.solver.active) >= self.element_budget:
                # Log detailed information about the budget violation after action
                element_count = len(self.solver.active)
                budget_usage_percent = (element_count / self.element_budget) * 100
                
                # print(f"\n===== POST-ACTION BUDGET EXCEEDED =====")
                # print(f"Current elements: {element_count}/{self.element_budget} ({budget_usage_percent:.1f}%)")
                # print(f"Action that caused violation: {mapped_action} ({self.action_names[mapped_action]})")
                # print(f"Change in elements: {pre_action_elements} -> {post_action_elements}")
                # print("=======================================\n")
                
                # Store pre-termination metrics
                info = {
                    'pre_termination_elements': element_count,
                    'budget_usage_percent': budget_usage_percent,
                    'violation_action': mapped_action,
                    'episode_steps': self._episode_steps
                }
                
                return self._end_episode(-1000.0, False, True, "Budget exceeded", info)
            

            # After adaptation and budget check, get post-adaptation state
            post_adapt_solution = self.solver.q.copy()
            post_adapt_grid = self.solver.coord.copy()
            post_adapt_resources = len(self.solver.active) / self.solver.max_elements

            # Check if action was actually applied by comparing element count before and after
            action_was_canceled = False
            if mapped_action == 1 and np.array_equal(old_active_elements, self.solver.active):
                action_was_canceled = True
                if self.debug_training_cycle:
                    print(f"Refinement was canceled for element {current_element}")
                
                # For canceled actions, set delta_u to 0
                delta_u_adapt = 0.0
            else:
                # Normal delta_u calculation for actions that were applied
                delta_u_adapt = calculate_delta_u(old_solution, post_adapt_solution, old_grid, post_adapt_grid)

            # Calculate adaptation-only reward
            reward = self.reward_calculator.calculate_reward(
                delta_u_adapt, 
                mapped_action,
                old_resources, 
                post_adapt_resources
            )
            
            # # Get post-adaptation state
            # post_adapt_solution = self.solver.q.copy()
            # post_adapt_grid = self.solver.coord.copy()
            # post_adapt_resources = len(self.solver.active) / self.solver.max_elements

            # # Calculate adaptation-only reward
            # delta_u_adapt = calculate_delta_u(old_solution, post_adapt_solution, old_grid, post_adapt_grid)

            # reward = self.reward_calculator.calculate_reward(
            #     delta_u_adapt, 
            #     mapped_action,
            #     old_resources, 
            #     post_adapt_resources
            # )

            # # Check if action was actually applied by comparing element count before and after
            # action_was_canceled = False
            # if mapped_action == 1 and np.array_equal(old_active_elements, self.solver.active):
            #     action_was_canceled = True
            #     if self.debug_training_cycle:
            #         print(f"Refinement was canceled for element {current_element}")
            

            if self.debug_training_cycle:
                # print(f"Applying adaptation for element {self.current_element_index} with action {mapped_action}")
                print(f"post adapt active: {self.solver.active}")
            
            # Determine if we should take a time step
            if self.rl_iterations_per_timestep == "random":
                # Randomly decide if we should take a time step
                if self.current_rl_iteration == 0:
                    self.iterations_before_timestep = np.random.randint(1, self.max_rl_iterations + 1)
                
                self.current_rl_iteration += 1
                self.should_timestep = (self.current_rl_iteration >= self.iterations_before_timestep)
                # After determining if we should take a time step
                if self.debug_training_cycle:
                    print(f"RL iteration {self.current_rl_iteration}/{self.iterations_before_timestep if self.rl_iterations_per_timestep == 'random' else self.rl_iterations_per_timestep}")
                    if self.should_timestep:
                        print("Taking solver time step")
            else:
                # Use fixed number of iterations
                self.current_rl_iteration = (self.current_rl_iteration + 1) % self.rl_iterations_per_timestep
                self.should_timestep = (self.current_rl_iteration == 0)
            
            # Take solver timestep only if it's time to do so
            if self.should_timestep:
                self.solver.step()
                self.current_rl_iteration = 0
                # Check if timestep caused budget violation
                if len(self.solver.active) >= self.element_budget:
                    element_count = len(self.solver.active)
                    budget_usage_percent = (element_count / self.element_budget) * 100
                    
                    print(f"\n===== TIMESTEP BUDGET EXCEEDED =====")
                    print(f"Current elements: {element_count}/{self.element_budget} ({budget_usage_percent:.1f}%)")
                    print(f"Previous action: {mapped_action} ({self.action_names[mapped_action]})")
                    print(f"Element progression: {pre_action_elements} -> {post_action_elements} -> {element_count}")
                    print("====================================\n")
                    
                    info = {
                        'pre_termination_elements': element_count,
                        'budget_usage_percent': budget_usage_percent,
                        'violation_action': mapped_action,
                        'timestep_violation': True,
                        'episode_steps': self._episode_steps
                    }
                    
                    return self._end_episode(-1000.0, False, True, "Budget exceeded (timestep)", info)
            
            # Get new state
            new_solution = self.solver.q
            new_grid = self.solver.coord
            new_resources = len(self.solver.active) / self.solver.max_elements

            # Special handling for canceled actions
            if action_was_canceled:
                # If the action was canceled, there should be no solution change
                delta_u = 0.0
                
                # Optional debugging to verify there's no solution change
                if self.debug_training_cycle:
                    # Calculate what delta_u would be normally
                    normal_delta_u = calculate_delta_u(old_solution, new_solution, old_grid, new_grid)
                    print(f"Action canceled but normal delta_u would be {normal_delta_u:.6f}")
                    print(f"Setting delta_u = 0 for canceled action")
            else:
                # Normal delta_u calculation for actions that were applied
                delta_u = calculate_delta_u(old_solution, new_solution, old_grid, new_grid)
            


            # delta_u = calculate_delta_u(old_solution, new_solution, old_grid, new_grid)
            
            # Compare solutions to calculate reward
            # Note: For accuracy, we should use the solution after mesh adaptation
            # but before time-stepping to isolate the effect of the adaptation
            # if len(new_solution) >= len(old_solution):
            #     old_interpolated = np.interp(new_grid, old_grid, old_solution)
            #     delta_u = np.linalg.norm(new_solution - old_interpolated)
            # else:
            #     new_interpolated = np.interp(old_grid, new_grid, new_solution)
            #     delta_u = np.linalg.norm(new_interpolated - old_solution)
                # When calculating reward, add penalty for unsafe refinement if needed

            # reward = self.reward_calculator.calculate_reward(
            #     delta_u, 
            #     mapped_action,  # Pass the mapped action (-1, 0, 1)
            #     old_resources, 
            #     new_resources
            # )

            if unsafe_refinement:
                reward -= 10.0  # Significant penalty for trying unsafe refinement
                if self.debug_training_cycle:
                    print(f"Applied unsafe refinement penalty. Reward: {reward:.2f}")
                
            terminated = False
            truncated = False
            # After calculating reward
            if self.debug_training_cycle:
                print(f"Active elements: {self.solver.active}")
                print(f"element: {current_element} | Action: {mapped_action} | Delta_u: {delta_u_adapt:.6f} | Reward: {reward:.4f}")
                print(f"Elements: {len(self.solver.active)}/{self.element_budget}")
            
            # Prepare info dictionary
            info = {
                'delta_u': delta_u,
                'resource_usage': new_resources,
                'n_elements': len(self.solver.active),
                'episode_steps': self._episode_steps,
                'total_steps': self.num_timesteps,
                'took_timestep': self.should_timestep
            }
            
            # Select next element randomly
            n_active = len(self.solver.active)
            if n_active > 0:
                self.current_element_index = np.random.randint(0, n_active)
            else:
                return self._end_episode(-100.0, False, True, "No active elements", None)
                
            # Get observation of new state
            observation = self._get_observation()
            
            return observation, reward, terminated, truncated, info
            
        except Exception as e:
            if self.verbose:
                print(f"Error in step: {e}")
            return self._end_episode(-100.0, False, True, f"Error: {str(e)}", None)
    
    def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
        """
        Reset environment with mesh quality checks and recovery strategies.
        
        Args:
            seed: Random seed
            options: Additional options
            
        Returns:
            tuple: (observation, info)
        """
        if self.verbose:
            print(f"\n--- STARTING EPISODE #{self._total_episodes + 1} ---\n")
        
        self._episode_steps = 0  # Reset episode counter
        super().reset(seed=seed)
        
        max_attempts = 3
        original_nelem = self.solver.nelem
        
        for attempt in range(max_attempts):
            try:
                # Try standard reset
                self.solver.reset()
                
                # Check mesh quality
                quality_ok, issues = self.solver.check_mesh_quality(self.solver.xelem)
                if not quality_ok:
                    if self.verbose:
                        print(f"Mesh quality issues detected: {issues}")
                    if attempt < max_attempts - 1:
                        raise ValueError(f"Poor mesh quality: {issues}")
                    
                # If we get here, reset was successful
                break
                
            except ValueError as e:
                if attempt < max_attempts - 1:
                    if self.verbose:
                        print(f"Reset failed attempt {attempt + 1}: {str(e)}")
                    
                    # Try different recovery strategies based on the error
                    if "condition number" in str(e):
                        # Strategy 1: Reduce number of elements
                        self.solver.nelem = max(4, self.solver.nelem - 2)
                        if self.verbose:
                            print(f"Trying with fewer elements: {self.solver.nelem}")
                        
                    elif "Poor mesh quality" in str(e):
                        # Strategy 2: Try uniform mesh
                        if self.verbose:
                            print("Trying uniform mesh distribution")
                        self.solver.xelem = np.linspace(
                            self.solver.xelem[0],
                            self.solver.xelem[-1],
                            self.solver.nelem + 1
                        )
                        
                    elif "Matrix solve failed" in str(e):
                        # Strategy 3: Increase polynomial order temporarily
                        if self.verbose:
                            print("Trying with increased polynomial order")
                        original_nop = self.solver.nop
                        self.solver.nop += 1
                        self.solver.ngl = self.solver.nop + 1
                    
                    else:
                        # Strategy 4: Reset to initial configuration
                        if self.verbose:
                            print("Resetting to initial configuration")
                        self.solver.nelem = original_nelem
                        self.solver.xelem = np.linspace(-1, 1, self.solver.nelem + 1)
                        
                    continue
                else:
                    if self.verbose:
                        print("Max reset attempts reached. Final configuration:")
                        print(f"Number of elements: {self.solver.nelem}")
                        print(f"Element sizes: {np.diff(self.solver.xelem)}")
                    raise
        
        # Reset was successful, select random initial element
        self.current_element_index = 0
        if len(self.solver.active) > 0:
            self.current_element_index = np.random.randint(0, len(self.solver.active))

        # Reset time-stepping variables
        self.current_rl_iteration = 0
        self.should_timestep = False
    
        # Prepare info dict with mesh quality metrics
        element_sizes = np.diff(self.solver.xelem)
        info = {
            'mesh_quality': {
                'min_element_size': np.min(element_sizes),
                'max_element_size': np.max(element_sizes),
                'size_ratio': np.max(element_sizes) / np.min(element_sizes),
                'n_elements': len(element_sizes),
                'total_episodes': self._total_episodes,
                'total_steps': self.num_timesteps
            }
        }
        
        observation = self._get_observation()
        return observation, info