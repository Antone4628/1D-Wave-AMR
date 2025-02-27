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
from ..solvers.dg_wave_solver import DGWaveSolver


class RewardCalculator:
    """
    Handles reward calculation for the AMR environment.
    """
    def __init__(self, gamma_c=25.0, machine_eps=1e-16):
        self.gamma_c = gamma_c
        self.machine_eps = machine_eps

    def calculate_resource_penalty(self, new_resources):
        """Calculate penalty for resource usage"""
        if new_resources >= 1.0:
            return 1000.0
        elif new_resources <= 0.0:
            return 0.0
        else:
            return self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)

    def calculate_reward(self, delta_u: float, new_resources: float) -> float:
        """
        Compute reward following paper's formulation.
        
        Args:
            delta_u: Change in solution after adaptation
            new_resources: New resource usage fraction
            
        Returns:
            float: Computed reward value
        """
        # Accuracy reward (log of solution change)
        accuracy = 3.0*np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
        # Resource penalty using barrier function
        resource_penalty = self.calculate_resource_penalty(new_resources)
        
        return float(accuracy - resource_penalty)


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
        max_episode_steps: int = 50,
        verbose: bool = False
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
        
        # Define observation space components
        self.observation_space = spaces.Dict({
            'local_jumps': spaces.Box(
                low=0.0,
                high=1e3,
                shape=(self.solver.ngl,), 
                dtype=np.float32
            ),
            'neighbor_jumps': spaces.Box(
                low=0.0,
                high=1e3,
                shape=(2,),
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
    
    def _get_observation(self) -> Dict[str, np.ndarray]:
        """
        Get current observation of the environment state.
        
        Returns:
            dict: Observation space components
        """
        # Get local solution jumps
        local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element_index)

        # Compute average jump across all elements
        all_jumps = []
        for i in range(len(self.solver.active)):
            jumps, _ = self._get_element_jumps(i)
            if not np.any(np.isnan(jumps)):
                all_jumps.append(jumps.mean())
    
        avg_jump = np.mean(all_jumps) if all_jumps else 0.0

        # Safety check for NaN values
        local_jumps = np.nan_to_num(local_jumps, 0.0)
        neighbor_jumps = np.nan_to_num(neighbor_jumps, 0.0)
        
        # Current resource usage
        resource_usage = len(self.solver.active) / self.element_budget

        # Get local solution values
        element_nodes = self.solver.intma[:, self.current_element_index]
        solution_values = self.solver.q[element_nodes]
    
        return {
            'local_jumps': local_jumps.astype(np.float32),
            'neighbor_jumps': neighbor_jumps.astype(np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }

    def _end_episode(self, reward, terminated, truncated, reason=""):
        """Helper method to handle episode ending logic"""
        observation = self._get_observation()
        
        info = {
            'episode_steps': self._episode_steps,
            'total_steps': self.num_timesteps,
            'reason': reason,
            'episode': {
                'r': float(reward),
                'l': int(max(1, self._episode_steps))
            }
        }
        
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
        Execute one step of the environment.
        """
        self.num_timesteps += 1
        self._episode_steps += 1

        # Map action
        action_int = action.item() if hasattr(action, 'item') else int(action)
        mapped_action = self.action_mapping[action_int]

        if self.verbose:
            print(f"\n{'='*50}")
            print(f"Episode #{self._total_episodes + 1}, Step #{self._episode_steps} (Total step #{self.num_timesteps})")
            print(f"Action: {mapped_action} ({'coarsen' if mapped_action == -1 else 'no change' if mapped_action == 0 else 'refine'})")
        
        # Check budget constraint
        if len(self.solver.active) >= self.element_budget:
            return self._end_episode(-1000.0, False, True, "Budget exceeded")
        
        # Check episode length constraint
        if self._episode_steps >= self.max_episode_steps:
            return self._end_episode(0.0, False, True, "Maximum episode steps reached")
        
        # Apply action to current element
        marks_override = {self.current_element_index: mapped_action}
        
        # Store initial state for reward calculation
        old_solution = self.solver.q.copy()
        old_grid = self.solver.coord.copy()
        old_resources = len(self.solver.active) / self.solver.max_elements

        try:
            # Apply adaptation
            self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
            
            # Take solver timestep
            self.solver.step()
            
            # Get new state
            new_solution = self.solver.q
            new_grid = self.solver.coord
            new_resources = len(self.solver.active) / self.solver.max_elements

            # Compare solutions to calculate reward
            if len(new_solution) >= len(old_solution):
                old_interpolated = np.interp(new_grid, old_grid, old_solution)
                delta_u = np.linalg.norm(new_solution - old_interpolated)
            else:
                new_interpolated = np.interp(old_grid, new_grid, new_solution)
                delta_u = np.linalg.norm(new_interpolated - old_solution)

            # Compute reward
            reward = self.reward_calculator.calculate_reward(delta_u, new_resources)
            terminated = False
            truncated = False

        except Exception as e:
            if self.verbose:
                print(f"Error in step: {e}")
            return self._end_episode(-100.0, False, True, f"Error: {str(e)}")
        
        # Prepare info dictionary
        info = {
            'delta_u': delta_u,
            'resource_usage': new_resources,
            'n_elements': len(self.solver.active),
            'episode_steps': self._episode_steps,
            'total_steps': self.num_timesteps
        }
        
        # Select next element randomly
        n_active = len(self.solver.active)
        if n_active > 0:
            self.current_element_index = np.random.randint(0, n_active)
            if self.verbose:
                print(f"Selected new element: {self.solver.active[self.current_element_index]} (index {self.current_element_index})")
        else:
            if self.verbose:
                print("Warning: No active elements!")
            return self._end_episode(-100.0, False, True, "No active elements")

        # Get observation of new state
        observation = self._get_observation()
        
        if self.verbose:
            print(f"Step {self.num_timesteps} completed.")
            print(f"{'='*50}\n")
        
        return observation, reward, terminated, truncated, info
    
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