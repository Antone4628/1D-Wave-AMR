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
        accuracy = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
        # Resource penalty using barrier function
        resource_penalty = self.calculate_resource_penalty(new_resources)
        
        return float(accuracy - resource_penalty)
# class RewardCalculator:
#     """Handles reward calculation with robust error handling."""
    
#     def __init__(self, gamma_c: float = 25.0, max_reward: float = 1000.0):
#         self.gamma_c = gamma_c
#         self.max_reward = max_reward
#         self.epsilon = np.finfo(float).eps
        
#     def calculate_solution_change_reward(self, delta_uh: float) -> float:
#         """Calculate reward based on solution change."""
#         try:
#             if abs(delta_uh) < self.epsilon:
#                 return 0.0
                
#             # Use log1p for better numerical stability
#             reward = np.log1p(abs(delta_uh))
#             return np.clip(reward, -self.max_reward, self.max_reward)
            
#         except Exception as e:
#             print(f"Error calculating solution change reward: {e}")
#             return 0.0
            
#     def calculate_resource_penalty(
#         self,
#         p_current: float,
#         p_next: float
#     ) -> float:
#         """Calculate penalty for resource usage."""
#         try:
#             if p_next >= 1.0:
#                 return self.max_reward
                
#             # Ensure values are in valid range
#             p_current = np.clip(p_current, 0.0, 0.99)
#             p_next = np.clip(p_next, 0.0, 0.99)
            
#             # Calculate penalty with better numerical stability
#             current_penalty = np.sqrt(p_current) / (1.0 - p_current)
#             next_penalty = np.sqrt(p_next) / (1.0 - p_next)
            
#             penalty = next_penalty - current_penalty
#             return np.clip(penalty, -self.max_reward, self.max_reward)
            
#         except Exception as e:
#             print(f"Error calculating resource penalty: {e}")
#             return self.max_reward
            
#     def __call__(
#         self,
#         action: int,
#         delta_uh: float,
#         p_current: float,
#         p_next: float
#     ) -> float:
#         """Calculate complete reward."""
#         try:
#             # Get base components
#             change_reward = self.calculate_solution_change_reward(delta_uh)
#             resource_penalty = self.calculate_resource_penalty(p_current, p_next)
            
#             # Calculate final reward based on action
#             if action == 0:  # Refine
#                 reward = change_reward - self.gamma_c * resource_penalty
#             elif action == 1:  # Coarsen
#                 reward = -change_reward - self.gamma_c * resource_penalty
#             else:  # No change
#                 reward = -self.gamma_c * resource_penalty
                
#             return float(np.clip(reward, -self.max_reward, self.max_reward))
            
#         except Exception as e:
#             print(f"Error in reward calculation: {e}")
#             return 0.0  # Safe fallback

class DGAMREnv(gym.Env):
    """
    Custom Environment for DG Wave AMR that follows Gymnasium interface.
    
    This environment allows an RL agent to make local mesh refinement decisions
    based on solution jumps and computational resources. Each step involves:
    1. Observing the current element's state (jumps, solution values)
    2. Choosing an action (refine, coarsen, or do nothing)
    3. Receiving a reward based on solution accuracy and resource usage
    
    Attributes:
        solver (DGWaveSolver): DG wave equation solver instance
        gamma_c (float): Cost penalty coefficient for reward function
        current_element (int): Index of current active element
        machine_eps (float): Machine epsilon for reward scaling
    """
    
    def __init__(
        self,
        solver: DGWaveSolver,
        element_budget: int,  # New parameter
        gamma_c: float = 25.0,
        render_mode: str = None,
        max_episode_steps: int = 50,
        
    ):
        """
        Initialize DG AMR environment with explicit element budget.

        Args:
            solver: Instance of DG wave solver
            gamma_c: Coefficient for resource penalty term in reward
            render_mode: Mode for visualization (if needed)
        """
   

        super().__init__()
        self.solver = solver
        self.element_budget = element_budget  # Store budget
        self.gamma_c = gamma_c
        self.render_mode = render_mode
        self.current_element_index = 0  # Changed name to be more explicit
        self.current_element = 0
        self.machine_eps = 1e-16
        self.max_episode_steps = max_episode_steps
        self.episode_callback = None  # Add this line

        # Initialize step counter and timing
        self._step_counter = 0
        self._step_start_time = time()

        # Add step tracking
        self.episode_rewards = []
        self.episode_lengths = []
        self.num_timesteps = 0
        self._episode_steps = 0
        self._total_episodes = 0

        # Initialize reward calculator
        self.reward_calculator = RewardCalculator(gamma_c=gamma_c)
        
        
        # Define action space as {0, 1, 2} which we'll map to {-1, 0, 1}
        # -1: coarsen
        #  0: do nothing
        #  1: refine
        self.action_space = spaces.Discrete(3)
        
        # Store action mapping for clarity
        self.action_mapping = {
            0: -1,  # coarsen
            1: 0,   # do nothing
            2: 1    # refine
        }
        
        # Define observation space components following paper
        self.observation_space = spaces.Dict({
            # Solution jumps at element boundaries and interior
            'local_jumps': spaces.Box(
            low=0.0,  # Jumps are absolute values, so minimum is 0
            high=1e3,  # Set reasonable maximum based on your solution range
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
                high=1.0,  # Resource usage is always between 0 and 1
                shape=(1,),
                dtype=np.float32
            ),
            'solution_values': spaces.Box(
                low=-1e3,  # Solution can be negative
                high=1e3,
                shape=(self.solver.ngl,),
                dtype=np.float32
            )
        })

    def register_callback(self, callback):
        """Register a callback to be called when episodes end."""
        self.episode_callback = callback
        print(f"Environment registered episode callback: {callback.__class__.__name__}")


    def _get_element_jumps(self, element_idx: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute solution jumps at element boundaries and interior nodes, accounting for periodicity.
        
        In a periodic domain, the first element's left neighbor is the last element,
        and the last element's right neighbor is the first element. This creates a
        continuous ring-like topology where jumps are calculated across all interfaces.
        
        Args:
            element_idx: Index of element in active_grid
                
        Returns:
            tuple: (local_jumps, neighbor_jumps)
                local_jumps: Array of jumps at each node [ngl]
                neighbor_jumps: Jumps at left and right interfaces [2]
        """
        # Safety check for valid element index
        if element_idx >= len(self.solver.active):
            print(f"Warning: Invalid element index {element_idx}, active elements: {len(self.solver.active)}")
            return np.zeros(self.solver.ngl), np.zeros(2)
            
        # Get element number from active grid
        elem = self.solver.active[element_idx]
        # print(f"\nProcessing element {elem} (index {element_idx})")
        
        # Extract solution values for current element
        elem_nodes = self.solver.intma[:, element_idx]
        elem_sol = self.solver.q[elem_nodes]
        # print(f"Element solution values: {elem_sol}")
        
        # Get boundary values for current element
        elem_left = elem_sol[0]
        elem_right = elem_sol[-1]
        # print(f"Element boundary values: left={elem_left:.6f}, right={elem_right:.6f}")
        
        # Initialize arrays for jumps
        local_jumps = np.zeros(self.solver.ngl)
        neighbor_jumps = np.zeros(2)
        
        try:
            # ====== Handle Left Neighbor (with periodicity) ======
            if elem > 1:
                # Normal case - left neighbor is element (elem-1)
                left_active_idx = np.where(self.solver.active == elem-1)[0]
                # print(f"Left neighbor is element {elem-1}")
            else:
                # Periodic case - first element's left neighbor is the last element
                left_active_idx = np.where(self.solver.active == len(self.solver.label_mat))[0]
                # print(f"Periodic left neighbor: connecting element {elem} to last element")
                
            if len(left_active_idx) > 0:
                left_idx = left_active_idx[0]
                left_nodes = self.solver.intma[:, left_idx]
                left_sol = self.solver.q[left_nodes]
                # print(f"Left neighbor solution values: {left_sol}")
                
                # Calculate jump at left interface
                local_jumps[0] = abs(elem_left - left_sol[-1])
                neighbor_jumps[0] = local_jumps[0]
                # print(f"Left interface jump: {local_jumps[0]:.6f}")
                        
            # ====== Handle Right Neighbor (with periodicity) ======
            if elem < len(self.solver.label_mat):
                # Normal case - right neighbor is element (elem+1)
                right_active_idx = np.where(self.solver.active == elem+1)[0]
                # print(f"Right neighbor is element {elem+1}")
            else:
                # Periodic case - last element's right neighbor is the first element
                right_active_idx = np.where(self.solver.active == 1)[0]
                # print(f"Periodic right neighbor: connecting element {elem} to first element")
                
            if len(right_active_idx) > 0:
                right_idx = right_active_idx[0]
                right_nodes = self.solver.intma[:, right_idx]
                right_sol = self.solver.q[right_nodes]
                # print(f"Right neighbor solution values: {right_sol}")
                
                # Calculate jump at right interface
                local_jumps[-1] = abs(elem_right - right_sol[0])
                neighbor_jumps[1] = local_jumps[-1]
                # print(f"Right interface jump: {local_jumps[-1]:.6f}")
                        
            # ====== Calculate Interior Jumps ======
            # print("Calculating interior jumps...")
            for i in range(1, self.solver.ngl-1):
                local_jumps[i] = abs(elem_sol[i] - elem_sol[i-1])
                # print(f"Interior jump {i}: {local_jumps[i]:.6f}")
                    
        except Exception as e:
            print(f"Error in _get_element_jumps: {e}")
            print(f"Element index: {element_idx}, Active elements: {len(self.solver.active)}")
            print(f"Stack trace:")
            import traceback
            traceback.print_exc()
            return np.zeros(self.solver.ngl), np.zeros(2)
        
        # print("\nFinal jump values:")
        # print(f"Local jumps: {local_jumps}")
        # print(f"Neighbor jumps: {neighbor_jumps}")
                
        return local_jumps, neighbor_jumps

    
    def _get_observation(self) -> Dict[str, np.ndarray]:
        """
        Get current observation of the environment state.
        
        Constructs observation following paper's formulation:
        1. Local solution jumps at current element
        2. Jumps at neighboring elements
        3. Average jump across all elements
        4. Current resource usage
        5. Local solution values
        
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
        # all_jumps = []
        # for i in range(len(self.solver.active)):
        #     jumps, _ = self._get_element_jumps(i)
        #     all_jumps.append(jumps.mean())
        # avg_jump = np.mean(all_jumps)
        
        # Current resource usage (fraction of max elements)
        # resource_usage = len(self.solver.active) / self.solver.max_elements
        resource_usage = len(self.solver.active) / self.element_budget

        # Get local solution values
        element_nodes = self.solver.intma[:, self.current_element_index]
        solution_values = self.solver.q[element_nodes]


        # Add debug prints before return
        # print("\nObservation debug:")
        # print(f"Local jumps: {local_jumps}")
        # print(f"Neighbor jumps: {neighbor_jumps}") 
        # print(f"Solution values: {self.solver.q[self.solver.intma[:, self.current_element]]}")
    
        
        return {
            'local_jumps': local_jumps.astype(np.float32),
            'neighbor_jumps': neighbor_jumps.astype(np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }


 
    def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
        """
        Execute one step of the environment.
        """
        self.num_timesteps += 1
        self._episode_steps += 1

        # Map action and prepare debug output
        action_int = action.item() if hasattr(action, 'item') else int(action)
        mapped_action = self.action_mapping[action_int]

        print(f"\n{'='*50}")
        # print(f"Step #{self.num_timesteps} (Episode step #{self._episode_steps})")
        print(f"Episode #{self._total_episodes + 1}, Step #{self._episode_steps} (Total step #{self.num_timesteps})")
        
        # Print initial state sizes
        print("\nInitial state:")
        print(f"Active elements: {self.solver.active.tolist()}")
        print(f"Solution vector size: {len(self.solver.q)}")
        print(f"intma shape: {self.solver.intma.shape}")
        print(f"npoin_dg: {self.solver.npoin_dg}")
        
        # Map action and prepare marks_override
        # mapped_action = self.action_mapping[action]
                # Check budget before any modifications
        if len(self.solver.active) >= self.element_budget:
            print(f"Budget exceeded! ({len(self.solver.active)} >= {self.element_budget})")
            observation = self._get_observation()
            reward = -1000.0
            truncated = True
            # info = {
            #     'budget_exceeded': True,
            #     'episode_steps': self._episode_steps,
            #     'total_steps': self.num_timesteps,
            #     'episode': {
            #         'r': reward,
            #         'l': self._episode_steps
            #     }
            # }
            # self._total_episodes += 1
            # return observation, reward, False, truncated, info
            info = {
                'budget_exceeded': True,  # or 'max_steps_exceeded': True
                'episode_steps': self._episode_steps,
                'total_steps': self.num_timesteps,
                'episode': {
                    'r': float(reward),  # Ensure reward is a float
                    'l': int(max(1, self._episode_steps))  # Ensure positive integer length
                }
            }
            self.episode_rewards.append(float(reward))
            self.episode_lengths.append(int(self._episode_steps))

            # Add debug prints
            print(f"ENV: Episode ending early - budget exceeded or max steps reached")
            print(f"ENV: Episode reward: {reward:.2f}, length: {self._episode_steps}")
            # Call the callback directly if registered
            if self.episode_callback is not None:
                print(f"ENV: Calling episode callback")
                self.episode_callback(reward, self._episode_steps)
            else:
                print(f"ENV: No episode callback registered")

            self._total_episodes += 1
            return observation, reward, False, truncated, info
        
        # Check if we've exceeded max episode steps
        if self._episode_steps >= self.max_episode_steps:
            print(f"Maximum episode length ({self.max_episode_steps} steps) reached, ending episode")
            observation = self._get_observation()
            reward = 0.0  # Neutral reward for hitting step limit
            truncated = True
            # info = {
            #     'max_steps_exceeded': True,
            #     'episode_steps': self._episode_steps,
            #     'total_steps': self.num_timesteps,
            #     'episode': {
            #         'r': reward,
            #         'l': self._episode_steps
            #     }
            # }
        
            # self._total_episodes += 1
            # return observation, reward, False, truncated, info
            info = {
                'budget_exceeded': True,  # or 'max_steps_exceeded': True
                'episode_steps': self._episode_steps,
                'total_steps': self.num_timesteps,
                'episode': {
                    'r': float(reward),  # Ensure reward is a float
                    'l': int(max(1, self._episode_steps))  # Ensure positive integer length
                }
            }
            self.episode_rewards.append(float(reward))
            self.episode_lengths.append(int(self._episode_steps))

            # Add debug prints
            print(f"ENV: Episode ending early - budget exceeded or max steps reached")
            print(f"ENV: Episode reward: {reward:.2f}, length: {self._episode_steps}")

            # Call the callback directly if registered
            if self.episode_callback is not None:
                print(f"ENV: Calling episode callback")
                self.episode_callback(reward, self._episode_steps)
            else:
                print(f"ENV: No episode callback registered")
            self._total_episodes += 1
            return observation, reward, False, truncated, info
        
        marks_override = {self.current_element_index: mapped_action}
        
        print(f"\nAction details:")
        print(f"Current element index: {self.current_element_index}")
        print(f"Action: {mapped_action} ({'coarsen' if mapped_action == -1 else 'no change' if mapped_action == 0 else 'refine'})")
        print(f"marks_override: {marks_override}")

        # Initialize reward and info
        reward = 0.0
        info = {}
        delta_u = 0.0
        budget_exceeded = False
        
        # Store initial state
        old_solution = self.solver.q.copy()
        old_grid = self.solver.coord.copy()
        old_resources = len(self.solver.active) / self.solver.max_elements

        try:
                    # Apply adaptation
            print("\nBefore adapt_mesh:")
            print(f"q size: {len(self.solver.q)}")
            print(f"active elements: {self.solver.active.tolist()}")
            
            self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
            
            print("\nAfter adapt_mesh:")
            print(f"q size: {len(self.solver.q)}")
            print(f"active elements: {self.solver.active.tolist()}")
            print(f"intma shape: {self.solver.intma.shape}")
            print(f"npoin_dg: {self.solver.npoin_dg}")
            
            # Take solver timestep
            self.solver.step()
            
            print("\nAfter solver step:")
            print(f"q size: {len(self.solver.q)}")
            print(f"active elements: {self.solver.active.tolist()}")
            print(f"intma shape: {self.solver.intma.shape}")
            # # Apply AMR action to current element  
            # marks_override = {self.current_element_index: action}
            # print(f'marks_override: {marks_override}')
            # print(f"Applying action {action} to element {current_element_number}")
            # self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)

            # print(f"After adapt_mesh:")
            # print(f"New active elements: {len(self.solver.active)}")
            # print(f"New active elements list: {self.solver.active.tolist()}")
            
            # # Take solver timestep
            # self.solver.step()
            
            # Get new state
            new_solution = self.solver.q
            new_grid = self.solver.coord
            new_resources = len(self.solver.active) / self.solver.max_elements

            # Compare solutions
            if len(new_solution) >= len(old_solution):
                old_interpolated = np.interp(new_grid, old_grid, old_solution)
                delta_u = np.linalg.norm(new_solution - old_interpolated)
            else:
                new_interpolated = np.interp(old_grid, new_grid, new_solution)
                delta_u = np.linalg.norm(new_interpolated - old_solution)

            # Compute reward using reward calculator
            reward = self.reward_calculator.calculate_reward(delta_u, new_resources)
            truncated = False

            # # Check if budget exceeded
            # budget_exceeded = len(self.solver.active) > self.element_budget

            # # Check budget before processing
            # if len(self.solver.active) >= self.element_budget:
            #     print(f"Budget exceeded! ({len(self.solver.active)} >= {self.element_budget})")
            #     observation = self._get_observation()  # Get current observation
            #     reward = -1000.0
            #     truncated = True
            #     info = {
            #         'budget_exceeded': True,
            #         'episode_steps': self._episode_steps,
            #         'total_steps': self.num_timesteps
            #     }
            #     return observation, reward, False, truncated, info
            # else:
            #     # Compare solutions
            #     if len(new_solution) >= len(old_solution):
            #         old_interpolated = np.interp(new_grid, old_grid, old_solution)
            #         delta_u = np.linalg.norm(new_solution - old_interpolated)
            #     else:
            #         new_interpolated = np.interp(old_grid, new_grid, new_solution)
            #         delta_u = np.linalg.norm(new_interpolated - old_solution)

            #     # Compute reward using reward calculator
            #     reward = self.reward_calculator.calculate_reward(delta_u, new_resources)
            #     truncated = False

        except Exception as e:
            print(f"Error in step: {e}")
            reward = -100.0  # Penalty for error
            truncated = True
            delta_u = 0.0
            new_resources = old_resources
            
        # Get observation of new state
        # observation = self._get_observation()
        
        # Always false as episodes don't end naturally
        terminated = False
        
        # Collect diagnostic information
        info = {
            'delta_u': delta_u,
            'resource_usage': new_resources if 'new_resources' in locals() else old_resources,
            'n_elements': len(self.solver.active),
            'step_call': self._step_counter,
            'episode_steps': self._episode_steps,
            'total_steps': self.num_timesteps
        }
        
        # Randomly select next element if continuing
        if not truncated:
            n_active = len(self.solver.active)
            if n_active > 0:
                # new_current = np.random.randint(0, n_active)
                # print(f"Selected new element: {self.solver.active[new_current]} out of {n_active} elements")
                # self.current_element_index = new_current
                # Ensure new index is valid
                self.current_element_index = np.random.randint(0, n_active)
                print(f"Selected new element: {self.solver.active[self.current_element_index]} (index {self.current_element_index}) out of {n_active} elements")
            else:
                print("Warning: No active elements!")
                self.current_element = 0
                reward = -100.0  # Penalty for invalid state
                truncated = True

        print(f"Step {self.num_timesteps} completed. New current_element: {self.solver.active[self.current_element_index]}")

        # Collect diagnostic information
        info = {
            'delta_u': delta_u,
            'resource_usage': new_resources if 'new_resources' in locals() else old_resources,
            'n_elements': len(self.solver.active),
            'step_call': self._step_counter,
            'episode_steps': self._episode_steps,
            'total_steps': self.num_timesteps
        }

        # Handle episode completion - make sure episode info is properly structured
        if terminated or truncated:
            # Ensure values are of correct types to avoid serialization issues
            eps_len = max(1, self._episode_steps)  # Ensure positive length
            
            # Add episode info directly to the info dictionary
            # info['episode'] = {
            #     'r': float(reward),  # Ensure reward is a float
            #     'l': int(eps_len)    # Ensure length is an integer
            # }
            # self.episode_rewards.append(float(reward))
            # self.episode_lengths.append(int(self._episode_steps))
            
            # # Add debug prints to verify info structure
            # print(f"ENV: Episode complete - adding episode info to info dict")
            # print(f"ENV: Episode reward: {reward:.2f}, length: {eps_len}")
            
            # # Increment episode counter
            # self._total_episodes += 1
            info = {
                'budget_exceeded': True,  # or 'max_steps_exceeded': True
                'episode_steps': self._episode_steps,
                'total_steps': self.num_timesteps,
                'episode': {
                    'r': float(reward),  # Ensure reward is a float
                    'l': int(max(1, self._episode_steps))  # Ensure positive integer length
                }
            }
            self.episode_rewards.append(float(reward))
            self.episode_lengths.append(int(self._episode_steps))

            # Add debug prints
            print(f"ENV: Episode ending early - budget exceeded or max steps reached")
            print(f"ENV: Episode reward: {reward:.2f}, length: {self._episode_steps}")

            # Call the callback directly if registered
            if self.episode_callback is not None:
                print(f"ENV: Calling episode callback")
                self.episode_callback(reward, self._episode_steps)
            else:
                print(f"ENV: No episode callback registered")
            self._total_episodes += 1

        # Get new observation
        observation = self._get_observation()

        print(f"Step {self.num_timesteps} completed. New current_element: {self.solver.active[self.current_element_index]}")
        print(f"{'='*50}\n")

        return observation, reward, terminated, truncated, info
        # # Get new observation
        # observation = self._get_observation()       
        # # Handle episode completion
        # if terminated or truncated:
        #     self._total_episodes += 1
        #     info['episode'] = {
        #         'r': reward,
        #         'l': self._episode_steps
        #     }
        
        # print(f"{'='*50}\n")
        
        # return observation, reward, terminated, truncated, info
    def plot_episodes(self, save_path):
        """Create a plot of tracked episodes."""
        if len(self.episode_rewards) == 0:
            return None
            
        plt.figure(figsize=(12, 5))
        
        # Plot rewards
        plt.subplot(1, 2, 1)
        plt.plot(self.episode_rewards, 'bo-')
        plt.title(f"Episode Rewards (Total: {self.episode_count})")
        plt.xlabel("Episode")
        plt.ylabel("Reward")
        plt.grid(True, alpha=0.3)
        
        # Plot lengths
        plt.subplot(1, 2, 2)
        plt.plot(self.episode_lengths, 'ro-')
        plt.title("Episode Lengths")
        plt.xlabel("Episode")
        plt.ylabel("Steps")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        return save_path   

    
    def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
        """
        Reset environment with mesh quality checks and recovery strategies.
        
        Args:
            seed: Random seed
            options: Additional options
            
        Returns:
            tuple: (observation, info)
        """
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
                    print(f"Mesh quality issues detected: {issues}")
                    if attempt < max_attempts - 1:
                        raise ValueError(f"Poor mesh quality: {issues}")
                    
                # If we get here, reset was successful
                break
                
            except ValueError as e:
                if attempt < max_attempts - 1:
                    print(f"Reset failed attempt {attempt + 1}: {str(e)}")
                    
                    # Try different recovery strategies based on the error
                    if "condition number" in str(e):
                        # Strategy 1: Reduce number of elements
                        self.solver.nelem = max(4, self.solver.nelem - 2)
                        print(f"Trying with fewer elements: {self.solver.nelem}")
                        
                    elif "Poor mesh quality" in str(e):
                        # Strategy 2: Try uniform mesh
                        print("Trying uniform mesh distribution")
                        domain_size = self.solver.xelem[-1] - self.solver.xelem[0]
                        self.solver.xelem = np.linspace(
                            self.solver.xelem[0],
                            self.solver.xelem[-1],
                            self.solver.nelem + 1
                        )
                        
                    elif "Matrix solve failed" in str(e):
                        # Strategy 3: Increase polynomial order temporarily
                        print("Trying with increased polynomial order")
                        original_nop = self.solver.nop
                        self.solver.nop += 1
                        self.solver.ngl = self.solver.nop + 1
                        # Note: Remember to reset nop after successful reset
                    
                    else:
                        # Strategy 4: Reset to initial configuration
                        print("Resetting to initial configuration")
                        self.solver.nelem = original_nelem
                        self.solver.xelem = np.linspace(-1, 1, self.solver.nelem + 1)
                        
                    continue
                else:
                    print("Max reset attempts reached. Final configuration:")
                    print(f"Number of elements: {self.solver.nelem}")
                    print(f"Element sizes: {np.diff(self.solver.xelem)}")
                    raise
        
        # Reset was successful, get initial state
        self.current_element = np.random.randint(0, len(self.solver.active))
        
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
        # Make sure it's a valid index for the newly reset environment
        self.current_element_index = 0
        if len(self.solver.active) > 0:
            self.current_element_index = np.random.randint(0, len(self.solver.active))
    
        
        observation = self._get_observation()
        
        # Add visualization of current mesh state if needed
        if self.render_mode == 'human':
            self._render_mesh_state()
            
        return observation, info

    def _render_mesh_state(self):
        """Visualize current mesh state and quality metrics"""
        import matplotlib.pyplot as plt
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot mesh
        element_sizes = np.diff(self.solver.xelem)
        ax1.plot(self.solver.xelem[:-1], element_sizes, 'b.-')
        ax1.set_title('Element Sizes')
        ax1.set_xlabel('Position')
        ax1.set_ylabel('Element Size')
        
        # Plot solution on mesh
        ax2.plot(self.solver.coord, self.solver.q, 'r.-')
        ax2.set_title('Solution')
        ax2.set_xlabel('Position')
        ax2.set_ylabel('Solution Value')
        
        # Add mesh quality metrics as text
        quality_ok, issues = self.check_mesh_quality(self.solver.xelem)
        if not quality_ok:
            ax1.text(0.02, 0.98, f"Quality Issues:\n{issues}", 
                    transform=ax1.transAxes, verticalalignment='top',
                    color='red')
        
        plt.tight_layout()
        plt.savefig(f'mesh_state_{self.reset_counter}.png')
        plt.close()








# """
# Custom Gymnasium Environment for DG Wave AMR following Foucart et al. (2023).

# This environment implements RL-based AMR for DG methods as described in:
# 'Deep reinforcement learning for adaptive mesh refinement'
# """

# import gymnasium as gym
# import numpy as np
# from gymnasium import spaces
# from ..solvers.dg_wave_solver import DGWaveSolver

# class DGAMREnv(gym.Env):
#     """
#     Custom Environment for DG Wave AMR that follows Gymnasium interface.
#     Implements specific observation and reward structure from Foucart et al. (2023).
#     """
    
#     def __init__(
#         self,
#         solver: DGWaveSolver,
#         gamma_c: float = 25.0,  # Cost penalty coefficient
#         render_mode=None
#     ):
#         """
#         Initialize environment.

#         Args:
#             solver: DG solver instance
#             gamma_c: Cost penalty coefficient for reward function
#             render_mode: Mode for rendering
#         """
#         super().__init__()
        
#         self.solver = solver
#         self.gamma_c = gamma_c
        
#         # Define action space: {coarsen, do nothing, refine}
#         self.action_space = spaces.Discrete(3)
        
#         # Define observation space following paper:
#         # 1. Local solution jumps at element boundaries
#         # 2. Average integrated jump across elements
#         # 3. Computational resource usage
#         # 4. Local solution values
#         self.observation_space = spaces.Dict({
#             'local_jumps': spaces.Box(
#                 low=-np.inf, 
#                 high=np.inf, 
#                 shape=(self.solver.ngl,), 
#                 dtype=np.float32
#             ),
#             'neighbor_jumps': spaces.Box(
#                 low=-np.inf,
#                 high=np.inf,
#                 shape=(2,),  # Left and right neighbor jumps
#                 dtype=np.float32
#             ),
#             'avg_jump': spaces.Box(
#                 low=-np.inf,
#                 high=np.inf,
#                 shape=(1,),
#                 dtype=np.float32
#             ),
#             'resource_usage': spaces.Box(
#                 low=0,
#                 high=1,
#                 shape=(1,),
#                 dtype=np.float32
#             ),
#             'solution_values': spaces.Box(
#                 low=-np.inf,
#                 high=np.inf,
#                 shape=(self.solver.ngl,),
#                 dtype=np.float32
#             )
#         })
        
#         self.current_element = 0
#         self.machine_eps = 1e-16  # For reward scaling
        
#     def _get_element_jumps(self, element_idx):
#         """
#         Compute solution jumps at element boundaries.
        
#         Args:
#             element_idx: Index of current element
            
#         Returns:
#             tuple: Local jumps and jumps at neighboring elements
#         """
#         # This should be implemented using your solver's methods
#         # to compute solution jumps at element interfaces
#         pass
        
#     def _get_observation(self):
#         """
#         Get current observation for the active element.
        
#         Returns:
#             dict: Observation following the paper's structure
#         """
#         # Get local solution jumps
#         local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element)
        
#         # Compute average jump across all elements
#         avg_jump = np.mean([
#             self._get_element_jumps(i)[0].mean() 
#             for i in range(self.solver.nelem)
#         ])
        
#         # Current resource usage (fraction of max elements used)
#         resource_usage = self.solver.nelem / self.solver.max_elements
        
#         # Local solution values
#         element_nodes = self.solver.intma[:, self.current_element]
#         solution_values = self.solver.q[element_nodes]
        
#         return {
#             'local_jumps': local_jumps.astype(np.float32),
#             'neighbor_jumps': neighbor_jumps.astype(np.float32),
#             'avg_jump': np.array([avg_jump], dtype=np.float32),
#             'resource_usage': np.array([resource_usage], dtype=np.float32),
#             'solution_values': solution_values.astype(np.float32)
#         }
        
#     def _compute_reward(self, delta_u, new_resources):
#         """
#         Compute reward following paper's formulation.
        
#         Args:
#             delta_u: Change in solution after adaptation
#             new_resources: New resource usage
            
#         Returns:
#             float: Computed reward
#         """
#         # Accuracy reward: log of solution change
#         accuracy = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
#         # Resource penalty using barrier function
#         resource_penalty = self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)
        
#         return accuracy - resource_penalty
        
#     def step(self, action):
#         """
#         Execute one step in the environment.
        
#         Args:
#             action: Element adaptation action (0=coarsen, 1=no change, 2=refine)
            
#         Returns:
#             tuple: (observation, reward, terminated, truncated, info)
#         """
#         # Store initial state
#         old_solution = self.solver.q.copy()
#         old_resources = self.solver.nelem / self.solver.max_elements
        
#         # Apply AMR action
#         if action == 0:  # Coarsen
#             self.solver.adapt_mesh(
#                 marks_override={self.current_element: -1}
#             )
#         elif action == 2:  # Refine
#             self.solver.adapt_mesh(
#                 marks_override={self.current_element: 1}
#             )
            
#         # Take solver timestep
#         self.solver.step()
        
#         # Compute change in solution
#         new_solution = self.solver.q
#         delta_u = np.linalg.norm(new_solution - old_solution)
        
#         # Get new resource usage
#         new_resources = self.solver.nelem / self.solver.max_elements
        
#         # Compute reward
#         reward = self._compute_reward(delta_u, new_resources)
        
#         # Get new observation
#         observation = self._get_observation()
        
#         # Check termination
#         terminated = False
#         truncated = (new_resources >= 1.0)
        
#         # Additional info for debugging
#         info = {
#             'delta_u': delta_u,
#             'resource_usage': new_resources,
#             'n_elements': self.solver.nelem
#         }
        
#         # Move to next element randomly
#         self.current_element = np.random.randint(0, self.solver.nelem)
        
#         return observation, reward, terminated, truncated, info
        
#     def reset(self, seed=None, options=None):
#         """
#         Reset environment to initial state.
        
#         Returns:
#             tuple: (observation, info)
#         """
#         super().reset(seed=seed)
        
#         # Reset solver to initial state
#         self.solver.reset()
        
#         # Start with random element
#         self.current_element = np.random.randint(0, self.solver.nelem)
        
#         return self._get_observation(), {}
        
#     def render(self):
#         """Render current state if requested."""
#         if self.render_mode is None:
#             return
            
#         # Implement visualization if needed
#         pass