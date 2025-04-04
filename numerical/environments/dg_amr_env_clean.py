"""
This environment implements reinforcement learning-based adaptive mesh refinement.

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
# from ..solvers.dg_wave_solver_clean import DGWaveSolver
from ..solvers.dg_wave_solver_free import DGWaveSolver


class RewardCalculator:
    """
    Handles reward calculation for the AMR environment following the paper's approach.
    Uses a barrier function B(p) = √p/(1-p) to penalize resource usage.
    """
    def __init__(self, gamma_c=25.0, machine_eps=1e-16):
        self.gamma_c = gamma_c
        self.machine_eps = machine_eps

    def calculate_barrier(self, p):
        """Calculate barrier function B(p) = √p/(1-p)"""
        if p >= 1.0:
            return float('inf')  
        elif p <= 0.0:
            return 0.0
        else:
            return np.sqrt(p) / (1 - p)  # Non-hortative barrier function
        

    def calculate_reward(self, delta_u, action, old_resources, new_resources):
        """
        Compute reward following paper's formulation (equation 5).
        """
        # Safety check for delta_u
        delta_u = 0.0 if np.isnan(delta_u) or np.isinf(delta_u) else delta_u
        
        # Base accuracy term (before applying sign)
        accuracy_term = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
        # Safety check for accuracy term
        accuracy_term = 0.0 if np.isnan(accuracy_term) or np.isinf(accuracy_term) else accuracy_term
        
        # Apply sign based on action (equation 5)
        if action == 1:  # refine
            accuracy = +accuracy_term
        elif action == -1:  # coarsen
            # coarsening_factor = 1.0
            coarsening_factor = 1.0
            accuracy = -accuracy_term*coarsening_factor
        else:  # do nothing
            accuracy = 0.0
        
        # Resource penalty using barrier function difference (equation 4)
        old_barrier = self.calculate_barrier(old_resources)
        new_barrier = self.calculate_barrier(new_resources)
        resource_penalty = new_barrier - old_barrier

            # Apply multiplier to resource penalty for coarsening
        if action == -1 and resource_penalty < 0:  # If coarsening and successful
            resource_multiplier = 1.0  # Increase the positive contribution by 50%
            resource_penalty *= resource_multiplier
        
        # Safety check for resource penalty
        resource_penalty = 0.0 if np.isnan(resource_penalty) or np.isinf(resource_penalty) else resource_penalty
        
        # Final calculation with safety
        reward = float(accuracy - self.gamma_c * resource_penalty)
        
        # print(f'delta_u: {delta_u}')
        # print(f'resource penalty: {resource_penalty}')
        # print(f'reward: {reward}')
        
        # Final safety check
        reward = 0.0 if np.isnan(reward) or np.isinf(reward) else reward
        
        return reward

    # def calculate_reward(self, delta_u: float, action: int, old_resources: float, new_resources: float) -> float:
    #     """
    #     Compute reward following paper's formulation (equation 5).
        
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
    Custom Environment for DG Wave AMR that follows the Gymnasium interface.
    
    This environment allows an RL agent to make local mesh refinement decisions
    based on solution jumps and computational resources. Following Foucart et al (2023),
    the environment models a POMDP where the agent observes a single element at a time
    and makes refinement decisions to balance accuracy vs computational cost.
    """
    
    def __init__(
        self,
        solver,
        element_budget: int,
        gamma_c: float = 25.0,
        render_mode: str = None,
        max_episode_steps: int = 200,
        verbose: bool = False,
        rl_iterations_per_timestep = "random",
        max_rl_iterations = 200,
        max_consecutive_no_action = 10,
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
            rl_iterations_per_timestep: "random" or fixed integer
            max_rl_iterations: Maximum RL iterations per timestep
            debug_training_cycle: Enable debugging info
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

        # Initialize no-action counter
        self.do_nothing_counter = 0
        self.max_consecutive_no_action = max_consecutive_no_action

        # Initialize reward calculator
        self.reward_calculator = RewardCalculator(gamma_c=gamma_c)
        
        # Track actions for debugging
        self.mapped_action_history = []
        
        # Define action space as {0, 1, 2} mapping to {-1, 0, 1}
        # -1: coarsen, 0: do nothing, 1: refine
        self.action_space = spaces.Discrete(3)
        self.action_mapping = {
            0: -1,  # coarsen
            1: 0,   # do nothing
            2: 1    # refine
        }

        # Parameters for time-stepping during training
        self.rl_iterations_per_timestep = rl_iterations_per_timestep
        self.max_rl_iterations = max_rl_iterations
        self.current_rl_iteration = 0
        self.should_timestep = False
        self.debug_training_cycle = debug_training_cycle
        
        # Define observation space following paper section 2.2.2
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
            'resource_usage': spaces.Box(
                low=0.0,
                high=1.0,
                shape=(1,),
                dtype=np.float32
            ),
            'solution_values': spaces.Box(
                low=-1e3,
                high=1e3,
                shape=(self.solver.ngl,),
                dtype=np.float32
            )
        })
        
        # Add an action name dictionary for logging
        self.action_names = {-1: "Coarsen", 0: "No Change", 1: "Refine"}

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
    #     Get observation following paper section 2.2.2, including:
    #     - Local average jump
    #     - Global average jump 
    #     - Resource usage
    #     - Local solution values
    #     """
    #     # Get local solution jumps
    #     local_jumps, _ = self._get_element_jumps(self.current_element_index)
        
    #     # Calculate average of local jumps for this element
    #     avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        
    #     # Compute average jump across all elements
    #     all_jumps = []
    #     for i in range(len(self.solver.active)):
    #         jumps, _ = self._get_element_jumps(i)
    #         if not np.any(np.isnan(jumps)):
    #             all_jumps.append(np.mean(jumps))
        
    #     avg_jump = np.mean(all_jumps) if all_jumps else 0.0
        
    #     # Current resource usage
    #     resource_usage = len(self.solver.active) / self.element_budget
        
    #     # Get local solution values
    #     element_nodes = self.solver.intma[:, self.current_element_index]
    #     solution_values = self.solver.q[element_nodes]
        
    #     return {
    #         'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
    #         'avg_jump': np.array([avg_jump], dtype=np.float32),
    #         'resource_usage': np.array([resource_usage], dtype=np.float32),
    #         'solution_values': solution_values.astype(np.float32)
    #     }
    def _get_observation(self):
        """
        Get observation following paper section 2.2.2, including:
        - Local average jump
        - Global average jump 
        - Resource usage
        - Local solution values
        """
        # Get local solution jumps
        local_jumps, _ = self._get_element_jumps(self.current_element_index)
        
        # Calculate average of local jumps for this element
        avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        
        # Add safety to prevent NaN
        avg_local_jump = 0.0 if np.isnan(avg_local_jump) else avg_local_jump
        
        # Compute average jump across all elements
        all_jumps = []
        for i in range(len(self.solver.active)):
            jumps, _ = self._get_element_jumps(i)
            if not np.any(np.isnan(jumps)):
                all_jumps.append(np.mean(jumps))
        
        avg_jump = np.mean(all_jumps) if all_jumps else 0.0
        
        # Add safety to prevent NaN
        avg_jump = 0.0 if np.isnan(avg_jump) else avg_jump
        
        # Current resource usage
        resource_usage = len(self.solver.active) / self.element_budget
        
        # Get local solution values
        element_nodes = self.solver.intma[:, self.current_element_index]
        solution_values = self.solver.q[element_nodes]
        
        # Safety check for solution values
        solution_values = np.nan_to_num(solution_values, nan=0.0, posinf=0.0, neginf=0.0)
        
        observation = {
            'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }
        
        return observation

    def _end_episode(self, reward, terminated, truncated, reason="", pre_term_info=None):
        """Helper method to handle episode ending logic"""
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
        
        # Calculate and log termination percentages periodically
        total_episodes = sum(self.termination_stats.values())
        if total_episodes % 10 == 0 and self.verbose:
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
            
        # Call callback if registered
        if self.episode_callback is not None:
            self.episode_callback(reward, self._episode_steps)
            
        self._total_episodes += 1
        return observation, reward, terminated, truncated, info
    
    def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
        """
        Execute one step of the environment following the paper's approach.
        """
        self.num_timesteps += 1
        self._episode_steps += 1
        if self.debug_training_cycle:
            print("-" * 50)
            print(f'timestep: {self.num_timesteps}')
        
        # Map action and log it for debugging
        action_int = action.item() if hasattr(action, 'item') else int(action)
        mapped_action = self.action_mapping[action_int]
        self.mapped_action_history.append(mapped_action)

            # Update do-nothing counter based on action
        if mapped_action == 0:  # do nothing
            self.do_nothing_counter += 1
            # Check if too many consecutive no-actions
            if self.do_nothing_counter > self.max_consecutive_no_action:
                # return self._end_episode(0.0, False, True, "Maximum consecutive no-actions reached")
                self.do_nothing_counter = 0 #reset the counter
                return self._end_episode(-100.0, False, True, "Maximum consecutive no-actions reached")
        else:
            self.do_nothing_counter = 0  # Reset counter when action is taken
        
        # Check episode length limit
        if self._episode_steps >= self.max_episode_steps:
            return self._end_episode(0.0, False, True, "Maximum episode steps reached")
        
        # Store current state for reward calculation
        old_solution = self.solver.q.copy()
        old_grid = self.solver.coord.copy()
        old_resources = len(self.solver.active) / self.element_budget
        
        # Budget check before action
        if len(self.solver.active) >= self.element_budget:
            info = {
                'pre_termination_elements': len(self.solver.active),
                'budget_usage_percent': (len(self.solver.active) / self.element_budget) * 100,
                'violation_action': mapped_action
            }
            
            return self._end_episode(-1000.0, False, True, "Budget exceeded (pre-action)", info)
        
        try:
            # Apply adaptation
            if self.debug_training_cycle:
                cur_elem = self.solver.active[self.current_element_index]
                # print(f"Applying action {mapped_action} to element {self.current_element_index}")
                print(f"Applying action {mapped_action} to element {cur_elem}")
                print(f"pre-action active: {self.solver.active}")

            # print(f"Applying action {mapped_action} to element {self.current_element_index}") 

            if self.current_element_index >= len(self.solver.active):
                print(f"ERROR: current_element_index ({self.current_element_index}) >= active length ({len(self.solver.active)}) ENVIRONMENT STEP")
                return self._end_episode(-100.0, False, True, "Index out of bounds")
            
            marks_override = {self.current_element_index: mapped_action}
            self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
            
            # Check budget after adaptation
            if len(self.solver.active) > self.element_budget:
                info = {
                    'pre_termination_elements': len(self.solver.active),
                    'budget_usage_percent': (len(self.solver.active) / self.element_budget) * 100,
                    'violation_action': mapped_action,
                    'step': 'post-adaptation'
                }
                
                return self._end_episode(-1000.0, False, True, "Budget exceeded (post-adapt)", info)
            
            # Get post-adaptation state
            post_adapt_solution = self.solver.q.copy()
            post_adapt_grid = self.solver.coord.copy()
            post_adapt_resources = len(self.solver.active) / self.element_budget
            
            # Calculate adaptation-specific delta_u
            delta_u_adapt = calculate_delta_u(old_solution, post_adapt_solution, old_grid, post_adapt_grid)
            
            # Calculate adaptation reward using the barrier function approach
            reward = self.reward_calculator.calculate_reward(
                delta_u_adapt, 
                mapped_action,
                old_resources, 
                post_adapt_resources
            )
            
            if self.debug_training_cycle:
                print(f"post-action active: {self.solver.active}")
                print(f"Delta_u: {delta_u_adapt}, Reward: {reward}")
                print(f"Elements: {len(self.solver.active)}/{self.element_budget}")
                
            
            # Determine if we should take a time step
            if self.rl_iterations_per_timestep == "random":
                # Randomly decide if we should take a time step
                if self.current_rl_iteration == 0:
                    self.iterations_before_timestep = np.random.randint(1, self.max_rl_iterations + 1)
                
                self.current_rl_iteration += 1
                self.should_timestep = (self.current_rl_iteration >= self.iterations_before_timestep)
                if self.debug_training_cycle:
                    print(f'Take timestep?: {self.should_timestep}')
                
                if self.debug_training_cycle and self.should_timestep:
                    print(f"Taking solver time step after {self.current_rl_iteration} RL iterations")
            else:
                # Use fixed number of iterations
                self.current_rl_iteration = (self.current_rl_iteration + 1) % self.rl_iterations_per_timestep
                self.should_timestep = (self.current_rl_iteration == 0)
            
            # Take solver timestep only if it's time to do so
            if self.should_timestep:
                # Store state before time step
                pre_step_solution = self.solver.q.copy()
                pre_step_grid = self.solver.coord.copy()
                
                # Take the time step
                self.solver.step()
                self.current_rl_iteration = 0
                
                # Check budget after time step
                if len(self.solver.active) > self.element_budget:
                    info = {
                        'pre_termination_elements': len(self.solver.active),
                        'budget_usage_percent': (len(self.solver.active) / self.element_budget) * 100,
                        'step': 'post-timestep'
                    }
                    
                    return self._end_episode(-1000.0, False, True, "Budget exceeded (post-timestep)", info)
            
            # Prepare info dictionary
            info = {
                'delta_u': delta_u_adapt,
                'resource_usage': post_adapt_resources,
                'n_elements': len(self.solver.active),
                'episode_steps': self._episode_steps,
                'total_steps': self.num_timesteps,
                'took_timestep': self.should_timestep
            }
            
            if self.debug_training_cycle:
                print("-" * 50)
                print('\n\n')
            # Select next element randomly
            n_active = len(self.solver.active)
            if n_active > 0:
                self.current_element_index = np.random.randint(0, n_active)
            else:
                return self._end_episode(-100.0, False, True, "No active elements")
                
            # Get observation of new state
            observation = self._get_observation()
            
            return observation, reward, False, False, info
            
        except Exception as e:
            if self.verbose:
                print(f"Error in step: {e}")
                import traceback
                traceback.print_exc()
            return self._end_episode(-100.0, False, True, f"Error: {str(e)}")




    def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
        """
        Reset environment to initial state with optional mesh refinement.
        
        Args:
            seed: Random seed
            options: Additional options including:
                - refinement_mode: Mode for initial mesh refinement ('none', 'fixed', 'random')
                - refinement_level: Level of initial refinement
                - refinement_probability: Probability for random refinement
                
        Returns:
            tuple: (observation, info)
        """
        if self.verbose:
            print(f"\n--- STARTING EPISODE #{self._total_episodes + 1} ---\n")
        
        self._episode_steps = 0  # Reset episode counter
        self.mapped_action_history = []  # Reset action history
        self.do_nothing_counter = 0  # Reset do-nothing counter
        super().reset(seed=seed)
        
        try:
            # Extract refinement options to pass to solver
            refinement_options = {}
            if options is not None:
                if 'refinement_mode' in options:
                    refinement_options['refinement_mode'] = options['refinement_mode']
                if 'refinement_level' in options:
                    refinement_options['refinement_level'] = options['refinement_level']
                if 'refinement_probability' in options:
                    refinement_options['refinement_probability'] = options['refinement_probability']
                
                if self.verbose:
                    print(f"Applying initial refinement: {refinement_options}")
            
            # Reset solver with refinement options
            self.solver.reset(**refinement_options)
            
            # Reset time-stepping variables
            self.current_rl_iteration = 0
            self.should_timestep = False
        
            # Prepare info dict
            element_sizes = np.diff(self.solver.xelem)
            active_levels = self._get_active_levels()
            
            # Add level distribution to info
            level_distribution = {}
            for level in range(self.solver.max_level + 1):
                level_distribution[level] = active_levels.count(level) if active_levels else 0
            
            info = {
                'mesh_quality': {
                    'min_element_size': np.min(element_sizes),
                    'max_element_size': np.max(element_sizes),
                    'size_ratio': np.max(element_sizes) / np.min(element_sizes),
                    'n_elements': len(element_sizes),
                    'total_episodes': self._total_episodes,
                    'total_steps': self.num_timesteps
                },
                'refinement_info': {
                    'mode': refinement_options.get('refinement_mode', 'none'),
                    'level': refinement_options.get('refinement_level', 0),
                    'resource_usage': len(self.solver.active) / self.element_budget,
                    'initial_elements': len(self.solver.active),
                    'level_distribution': level_distribution
                }
            }
            
            # Randomly select initial element
            if len(self.solver.active) > 0:
                self.current_element_index = np.random.randint(0, len(self.solver.active))
        
            # Get initial observation
            observation = self._get_observation()
            
            return observation, info
            
        except Exception as e:
            if self.verbose:
                print(f"Reset error: {e}")
                import traceback
                traceback.print_exc()
            
            # Create a basic observation in case of error
            observation = self._get_observation()
            info = {'reset_error': str(e)}
            
            return observation, info

    def _get_active_levels(self):
        """Get refinement levels for active elements."""
        active_levels = []
        for elem in self.solver.active:
            # Element number in active grid is 1-indexed, so subtract 1 for label_mat
            level = self.solver.label_mat[elem-1][4]  # Level is stored in column 4
            active_levels.append(level)
        return active_levels   
    # def reset(self, seed=None, options=None):
    #     """
    #     Reset environment to initial state.
        
    #     Args:
    #         seed: Random seed
    #         options: Additional options including:
    #             - refinement_mode: Mode for initial mesh refinement
    #             - refinement_level: Level of initial refinement
    #             - refinement_probability: Probability for random refinement
                
    #     Returns:
    #         tuple: (observation, info)
    #     """
    #     if self.verbose:
    #         print(f"\n--- STARTING EPISODE #{self._total_episodes + 1} ---\n")
        
    #     self._episode_steps = 0  # Reset episode counter
    #     self.mapped_action_history = []  # Reset action history
    #     self.do_nothing_counter = 0  # Reset do-nothing counter
    #     super().reset(seed=seed)
        
    #     # Extract refinement options
    #     if options is None:
    #         options = {}
        
    #     refinement_mode = options.get('refinement_mode', 'none')
    #     refinement_level = options.get('refinement_level', 0)
    #     refinement_probability = options.get('refinement_probability', 0.5)
        
    #     try:
    #         # Reset solver with specified refinement
    #         self.solver.reset(
    #             refinement_mode=refinement_mode,
    #             refinement_level=refinement_level,
    #             refinement_probability=refinement_probability
    #         )
            
    #         # Reset time-stepping variables
    #         self.current_rl_iteration = 0
    #         self.should_timestep = False
        
    #         # Prepare info dict
    #         element_sizes = np.diff(self.solver.xelem)
    #         info = {
    #             'mesh_quality': {
    #                 'min_element_size': np.min(element_sizes),
    #                 'max_element_size': np.max(element_sizes),
    #                 'size_ratio': np.max(element_sizes) / np.min(element_sizes),
    #                 'n_elements': len(element_sizes),
    #                 'total_episodes': self._total_episodes,
    #                 'total_steps': self.num_timesteps
    #             },
    #             'refinement_info': {
    #                 'mode': refinement_mode,
    #                 'level': refinement_level,
    #                 'resource_usage': len(self.solver.active) / self.element_budget
    #             }
    #         }
            
    #         # Randomly select initial element
    #         if len(self.solver.active) > 0:
    #             self.current_element_index = np.random.randint(0, len(self.solver.active))
        
    #         # Get initial observation
    #         observation = self._get_observation()
            
    #         return observation, info
            
    #     except Exception as e:
    #         if self.verbose:
    #             print(f"Reset error: {e}")
    #             import traceback
    #             traceback.print_exc()
            
    #         # Create a basic observation in case of error
    #         observation = self._get_observation()
    #         info = {'reset_error': str(e)}
            
    #         return observation, info
    
    # def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    #     """
    #     Reset environment to initial state.
        
    #     Args:
    #         seed: Random seed
    #         options: Additional options
            
    #     Returns:
    #         tuple: (observation, info)
    #     """
    #     if self.verbose:
    #         print(f"\n--- STARTING EPISODE #{self._total_episodes + 1} ---\n")
        
    #     self._episode_steps = 0  # Reset episode counter
    #     self.mapped_action_history = []  # Reset action history
    #     self.do_nothing_counter = 0  # Reset do-nothing counter
    #     super().reset(seed=seed)
        
    #     try:
    #         # Reset solver to initial condition
    #         self.solver.reset()
            
    #         # Reset time-stepping variables
    #         self.current_rl_iteration = 0
    #         self.should_timestep = False
        
    #         # Prepare info dict
    #         element_sizes = np.diff(self.solver.xelem)
    #         info = {
    #             'mesh_quality': {
    #                 'min_element_size': np.min(element_sizes),
    #                 'max_element_size': np.max(element_sizes),
    #                 'size_ratio': np.max(element_sizes) / np.min(element_sizes),
    #                 'n_elements': len(element_sizes),
    #                 'total_episodes': self._total_episodes,
    #                 'total_steps': self.num_timesteps
    #             }
    #         }
            
    #         # Randomly select initial element
    #         if len(self.solver.active) > 0:
    #             self.current_element_index = np.random.randint(0, len(self.solver.active))
        
    #         # Get initial observation
    #         observation = self._get_observation()
            
    #         return observation, info
            
    #     except Exception as e:
    #         if self.verbose:
    #             print(f"Reset error: {e}")
    #             import traceback
    #             traceback.print_exc()
            
    #         # Create a basic observation in case of error
    #         observation = self._get_observation()
    #         info = {'reset_error': str(e)}
            
    #         return observation, info
            
    def render(self):
        """Rendering is not implemented for this environment."""
        pass
        
    def close(self):
        """Close environment resources."""
        pass






# """
# This environment implements reinforcement learning-based adaptive mesh refinement 
# for discontinuous Galerkin methods.

# The environment provides:
# - Observation space based on solution jumps and resource usage
# - Action space for element refinement decisions
# - Reward function balancing accuracy and computational cost
# """

# import gymnasium as gym
# import numpy as np
# from gymnasium import spaces
# from time import time
# from typing import Optional, Dict, Tuple, Any
# import matplotlib.pyplot as plt
# from ..solvers.dg_wave_solver import DGWaveSolver


# class RewardCalculator:
#     """
#     Handles reward calculation for the AMR environment.
#     """
#     def __init__(self, gamma_c=25.0, machine_eps=1e-16):
#         self.gamma_c = gamma_c
#         self.machine_eps = machine_eps

#     def calculate_resource_penalty(self, new_resources):
#         """Calculate penalty for resource usage"""
#         if new_resources >= 1.0:
#             return 1000.0
#         elif new_resources <= 0.0:
#             return 0.0
#         else:
#             return self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)

#     def calculate_reward(self, delta_u: float, new_resources: float) -> float:
#         """
#         Compute reward following paper's formulation.
        
#         Args:
#             delta_u: Change in solution after adaptation
#             new_resources: New resource usage fraction
            
#         Returns:
#             float: Computed reward value
#         """
#         # Accuracy reward (log of solution change)
#         accuracy = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
#         # Resource penalty using barrier function
#         resource_penalty = self.calculate_resource_penalty(new_resources)
        
#         return float(accuracy - resource_penalty)


# class DGAMREnv(gym.Env):
#     """
#     Custom Environment for DG Wave AMR that follows Gymnasium interface.
    
#     This environment allows an RL agent to make local mesh refinement decisions
#     based on solution jumps and computational resources. Each step involves:
#     1. Observing the current element's state (jumps, solution values)
#     2. Choosing an action (refine, coarsen, or do nothing)
#     3. Receiving a reward based on solution accuracy and resource usage
#     """
    
#     def __init__(
#         self,
#         solver: DGWaveSolver,
#         element_budget: int,
#         gamma_c: float = 25.0,
#         render_mode: str = None,
#         max_episode_steps: int = 50,
#         verbose: bool = False
#     ):
#         """
#         Initialize DG AMR environment with explicit element budget.

#         Args:
#             solver: Instance of DG wave solver
#             element_budget: Maximum number of elements allowed
#             gamma_c: Coefficient for resource penalty term in reward
#             render_mode: Mode for visualization (if needed)
#             max_episode_steps: Maximum steps per episode
#             verbose: Whether to print detailed logs
#         """
#         super().__init__()
#         self.solver = solver
#         self.element_budget = element_budget
#         self.gamma_c = gamma_c
#         self.render_mode = render_mode
#         self.current_element_index = 0
#         self.machine_eps = 1e-16
#         self.max_episode_steps = max_episode_steps
#         self.episode_callback = None
#         self.verbose = verbose

#         # Initialize step counters
#         self.num_timesteps = 0
#         self._episode_steps = 0
#         self._total_episodes = 0

#         # Initialize reward calculator
#         self.reward_calculator = RewardCalculator(gamma_c=gamma_c)
        
#         # Define action space as {0, 1, 2} mapping to {-1, 0, 1}
#         # -1: coarsen, 0: do nothing, 1: refine
#         self.action_space = spaces.Discrete(3)
#         self.action_mapping = {
#             0: -1,  # coarsen
#             1: 0,   # do nothing
#             2: 1    # refine
#         }
        
#         # Define observation space components
#         self.observation_space = spaces.Dict({
#             'local_jumps': spaces.Box(
#                 low=0.0,
#                 high=1e3,
#                 shape=(self.solver.ngl,), 
#                 dtype=np.float32
#             ),
#             'neighbor_jumps': spaces.Box(
#                 low=0.0,
#                 high=1e3,
#                 shape=(2,),
#                 dtype=np.float32
#             ),
#             'avg_jump': spaces.Box(
#                 low=0.0,
#                 high=1e3,
#                 shape=(1,),
#                 dtype=np.float32
#             ),
#             'resource_usage': spaces.Box(
#                 low=0.0,
#                 high=1.0,
#                 shape=(1,),
#                 dtype=np.float32
#             ),
#             'solution_values': spaces.Box(
#                 low=-1e3,
#                 high=1e3,
#                 shape=(self.solver.ngl,),
#                 dtype=np.float32
#             )
#         })

#     def register_callback(self, callback):
#         """Register a callback to be called when episodes end."""
#         self.episode_callback = callback
#         if self.verbose:
#             print(f"Environment registered episode callback: {callback.__class__.__name__}")

#     def _get_element_jumps(self, element_idx: int) -> Tuple[np.ndarray, np.ndarray]:
#         """
#         Compute solution jumps at element boundaries and interior nodes.
        
#         Args:
#             element_idx: Index of element in active_grid
                
#         Returns:
#             tuple: (local_jumps, neighbor_jumps)
#         """
#         # Safety check for valid element index
#         if element_idx >= len(self.solver.active):
#             if self.verbose:
#                 print(f"Warning: Invalid element index {element_idx}, active elements: {len(self.solver.active)}")
#             return np.zeros(self.solver.ngl), np.zeros(2)
            
#         # Get element number from active grid
#         elem = self.solver.active[element_idx]
        
#         # Extract solution values for current element
#         elem_nodes = self.solver.intma[:, element_idx]
#         elem_sol = self.solver.q[elem_nodes]
        
#         # Get boundary values
#         elem_left = elem_sol[0]
#         elem_right = elem_sol[-1]
        
#         # Initialize arrays for jumps
#         local_jumps = np.zeros(self.solver.ngl)
#         neighbor_jumps = np.zeros(2)
        
#         try:
#             # Handle Left Neighbor (with periodicity)
#             if elem > 1:
#                 left_active_idx = np.where(self.solver.active == elem-1)[0]
#             else:
#                 left_active_idx = np.where(self.solver.active == len(self.solver.label_mat))[0]
                
#             if len(left_active_idx) > 0:
#                 left_idx = left_active_idx[0]
#                 left_nodes = self.solver.intma[:, left_idx]
#                 left_sol = self.solver.q[left_nodes]
                
#                 # Calculate jump at left interface
#                 local_jumps[0] = abs(elem_left - left_sol[-1])
#                 neighbor_jumps[0] = local_jumps[0]
                        
#             # Handle Right Neighbor (with periodicity)
#             if elem < len(self.solver.label_mat):
#                 right_active_idx = np.where(self.solver.active == elem+1)[0]
#             else:
#                 right_active_idx = np.where(self.solver.active == 1)[0]
                
#             if len(right_active_idx) > 0:
#                 right_idx = right_active_idx[0]
#                 right_nodes = self.solver.intma[:, right_idx]
#                 right_sol = self.solver.q[right_nodes]
                
#                 # Calculate jump at right interface
#                 local_jumps[-1] = abs(elem_right - right_sol[0])
#                 neighbor_jumps[1] = local_jumps[-1]
                        
#             # Calculate Interior Jumps
#             for i in range(1, self.solver.ngl-1):
#                 local_jumps[i] = abs(elem_sol[i] - elem_sol[i-1])
                    
#         except Exception as e:
#             if self.verbose:
#                 print(f"Error in _get_element_jumps: {e}")
#                 import traceback
#                 traceback.print_exc()
#             return np.zeros(self.solver.ngl), np.zeros(2)
                
#         return local_jumps, neighbor_jumps
    
#     def _get_observation(self) -> Dict[str, np.ndarray]:
#         """
#         Get current observation of the environment state.
        
#         Returns:
#             dict: Observation space components
#         """
#         # Get local solution jumps
#         local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element_index)

#         # Compute average jump across all elements
#         all_jumps = []
#         for i in range(len(self.solver.active)):
#             jumps, _ = self._get_element_jumps(i)
#             if not np.any(np.isnan(jumps)):
#                 all_jumps.append(jumps.mean())
    
#         avg_jump = np.mean(all_jumps) if all_jumps else 0.0

#         # Safety check for NaN values
#         local_jumps = np.nan_to_num(local_jumps, 0.0)
#         neighbor_jumps = np.nan_to_num(neighbor_jumps, 0.0)
        
#         # Current resource usage
#         resource_usage = len(self.solver.active) / self.element_budget

#         # Get local solution values
#         element_nodes = self.solver.intma[:, self.current_element_index]
#         solution_values = self.solver.q[element_nodes]
    
#         return {
#             'local_jumps': local_jumps.astype(np.float32),
#             'neighbor_jumps': neighbor_jumps.astype(np.float32),
#             'avg_jump': np.array([avg_jump], dtype=np.float32),
#             'resource_usage': np.array([resource_usage], dtype=np.float32),
#             'solution_values': solution_values.astype(np.float32)
#         }

#     def _end_episode(self, reward, terminated, truncated, reason=""):
#         """Helper method to handle episode ending logic"""
#         observation = self._get_observation()
        
#         info = {
#             'episode_steps': self._episode_steps,
#             'total_steps': self.num_timesteps,
#             'reason': reason,
#             'episode': {
#                 'r': float(reward),
#                 'l': int(max(1, self._episode_steps))
#             }
#         }
        
#         if self.verbose:
#             print(f"Episode ending: {reason}")
#             print(f"Episode reward: {reward:.2f}, length: {self._episode_steps}")

#         # Call callback if registered
#         if self.episode_callback is not None:
#             self.episode_callback(reward, self._episode_steps)
            
#         self._total_episodes += 1
#         return observation, reward, terminated, truncated, info

#     def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
#         """
#         Execute one step of the environment.
#         """
#         self.num_timesteps += 1
#         self._episode_steps += 1

#         # Map action
#         action_int = action.item() if hasattr(action, 'item') else int(action)
#         mapped_action = self.action_mapping[action_int]

#         if self.verbose:
#             print(f"\n{'='*50}")
#             print(f"Episode #{self._total_episodes + 1}, Step #{self._episode_steps} (Total step #{self.num_timesteps})")
#             print(f"Action: {mapped_action} ({'coarsen' if mapped_action == -1 else 'no change' if mapped_action == 0 else 'refine'})")
        
#         # Check budget constraint
#         if len(self.solver.active) >= self.element_budget:
#             return self._end_episode(-1000.0, False, True, "Budget exceeded")
        
#         # Check episode length constraint
#         if self._episode_steps >= self.max_episode_steps:
#             return self._end_episode(0.0, False, True, "Maximum episode steps reached")
        
#         # Apply action to current element
#         marks_override = {self.current_element_index: mapped_action}
        
#         # Store initial state for reward calculation
#         old_solution = self.solver.q.copy()
#         old_grid = self.solver.coord.copy()
#         old_resources = len(self.solver.active) / self.solver.max_elements

#         try:
#             # Apply adaptation
#             self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
            
#             # Take solver timestep
#             self.solver.step()
            
#             # Get new state
#             new_solution = self.solver.q
#             new_grid = self.solver.coord
#             new_resources = len(self.solver.active) / self.solver.max_elements

#             # Compare solutions to calculate reward
#             if len(new_solution) >= len(old_solution):
#                 old_interpolated = np.interp(new_grid, old_grid, old_solution)
#                 delta_u = np.linalg.norm(new_solution - old_interpolated)
#             else:
#                 new_interpolated = np.interp(old_grid, new_grid, new_solution)
#                 delta_u = np.linalg.norm(new_interpolated - old_solution)

#             # Compute reward
#             reward = self.reward_calculator.calculate_reward(delta_u, new_resources)
#             terminated = False
#             truncated = False

#         except Exception as e:
#             if self.verbose:
#                 print(f"Error in step: {e}")
#             return self._end_episode(-100.0, False, True, f"Error: {str(e)}")
        
#         # Prepare info dictionary
#         info = {
#             'delta_u': delta_u,
#             'resource_usage': new_resources,
#             'n_elements': len(self.solver.active),
#             'episode_steps': self._episode_steps,
#             'total_steps': self.num_timesteps
#         }
        
#         # Select next element randomly
#         n_active = len(self.solver.active)
#         if n_active > 0:
#             self.current_element_index = np.random.randint(0, n_active)
#             if self.verbose:
#                 print(f"Selected new element: {self.solver.active[self.current_element_index]} (index {self.current_element_index})")
#         else:
#             if self.verbose:
#                 print("Warning: No active elements!")
#             return self._end_episode(-100.0, False, True, "No active elements")

#         # Get observation of new state
#         observation = self._get_observation()
        
#         if self.verbose:
#             print(f"Step {self.num_timesteps} completed.")
#             print(f"{'='*50}\n")
        
#         return observation, reward, terminated, truncated, info
    
#     def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
#         """
#         Reset environment with mesh quality checks and recovery strategies.
        
#         Args:
#             seed: Random seed
#             options: Additional options
            
#         Returns:
#             tuple: (observation, info)
#         """
#         if self.verbose:
#             print(f"\n--- STARTING EPISODE #{self._total_episodes + 1} ---\n")
        
#         self._episode_steps = 0  # Reset episode counter
#         super().reset(seed=seed)
        
#         max_attempts = 3
#         original_nelem = self.solver.nelem
        
#         for attempt in range(max_attempts):
#             try:
#                 # Try standard reset
#                 self.solver.reset()
                
#                 # Check mesh quality
#                 quality_ok, issues = self.solver.check_mesh_quality(self.solver.xelem)
#                 if not quality_ok:
#                     if self.verbose:
#                         print(f"Mesh quality issues detected: {issues}")
#                     if attempt < max_attempts - 1:
#                         raise ValueError(f"Poor mesh quality: {issues}")
                    
#                 # If we get here, reset was successful
#                 break
                
#             except ValueError as e:
#                 if attempt < max_attempts - 1:
#                     if self.verbose:
#                         print(f"Reset failed attempt {attempt + 1}: {str(e)}")
                    
#                     # Try different recovery strategies based on the error
#                     if "condition number" in str(e):
#                         # Strategy 1: Reduce number of elements
#                         self.solver.nelem = max(4, self.solver.nelem - 2)
#                         if self.verbose:
#                             print(f"Trying with fewer elements: {self.solver.nelem}")
                        
#                     elif "Poor mesh quality" in str(e):
#                         # Strategy 2: Try uniform mesh
#                         if self.verbose:
#                             print("Trying uniform mesh distribution")
#                         self.solver.xelem = np.linspace(
#                             self.solver.xelem[0],
#                             self.solver.xelem[-1],
#                             self.solver.nelem + 1
#                         )
                        
#                     elif "Matrix solve failed" in str(e):
#                         # Strategy 3: Increase polynomial order temporarily
#                         if self.verbose:
#                             print("Trying with increased polynomial order")
#                         original_nop = self.solver.nop
#                         self.solver.nop += 1
#                         self.solver.ngl = self.solver.nop + 1
                    
#                     else:
#                         # Strategy 4: Reset to initial configuration
#                         if self.verbose:
#                             print("Resetting to initial configuration")
#                         self.solver.nelem = original_nelem
#                         self.solver.xelem = np.linspace(-1, 1, self.solver.nelem + 1)
                        
#                     continue
#                 else:
#                     if self.verbose:
#                         print("Max reset attempts reached. Final configuration:")
#                         print(f"Number of elements: {self.solver.nelem}")
#                         print(f"Element sizes: {np.diff(self.solver.xelem)}")
#                     raise
        
#         # Reset was successful, select random initial element
#         self.current_element_index = 0
#         if len(self.solver.active) > 0:
#             self.current_element_index = np.random.randint(0, len(self.solver.active))
    
#         # Prepare info dict with mesh quality metrics
#         element_sizes = np.diff(self.solver.xelem)
#         info = {
#             'mesh_quality': {
#                 'min_element_size': np.min(element_sizes),
#                 'max_element_size': np.max(element_sizes),
#                 'size_ratio': np.max(element_sizes) / np.min(element_sizes),
#                 'n_elements': len(element_sizes),
#                 'total_episodes': self._total_episodes,
#                 'total_steps': self.num_timesteps
#             }
#         }
        
#         observation = self._get_observation()
#         return observation, info