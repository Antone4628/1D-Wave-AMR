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
from typing import Dict, Tuple, Any
from ..solvers.dg_wave_solver import DGWaveSolver

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
        render_mode: str = None
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
        self.current_element = 0
        self.machine_eps = 1e-16
        
        # Define action space: {coarsen (-1), do nothing (0), refine (1)}
        self.action_space = spaces.Discrete(3)
        
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
        print(f"\nProcessing element {elem} (index {element_idx})")
        
        # Extract solution values for current element
        elem_nodes = self.solver.intma[:, element_idx]
        elem_sol = self.solver.q[elem_nodes]
        print(f"Element solution values: {elem_sol}")
        
        # Get boundary values for current element
        elem_left = elem_sol[0]
        elem_right = elem_sol[-1]
        print(f"Element boundary values: left={elem_left:.6f}, right={elem_right:.6f}")
        
        # Initialize arrays for jumps
        local_jumps = np.zeros(self.solver.ngl)
        neighbor_jumps = np.zeros(2)
        
        try:
            # ====== Handle Left Neighbor (with periodicity) ======
            if elem > 1:
                # Normal case - left neighbor is element (elem-1)
                left_active_idx = np.where(self.solver.active == elem-1)[0]
                print(f"Left neighbor is element {elem-1}")
            else:
                # Periodic case - first element's left neighbor is the last element
                left_active_idx = np.where(self.solver.active == len(self.solver.label_mat))[0]
                print(f"Periodic left neighbor: connecting element {elem} to last element")
                
            if len(left_active_idx) > 0:
                left_idx = left_active_idx[0]
                left_nodes = self.solver.intma[:, left_idx]
                left_sol = self.solver.q[left_nodes]
                print(f"Left neighbor solution values: {left_sol}")
                
                # Calculate jump at left interface
                local_jumps[0] = abs(elem_left - left_sol[-1])
                neighbor_jumps[0] = local_jumps[0]
                print(f"Left interface jump: {local_jumps[0]:.6f}")
                        
            # ====== Handle Right Neighbor (with periodicity) ======
            if elem < len(self.solver.label_mat):
                # Normal case - right neighbor is element (elem+1)
                right_active_idx = np.where(self.solver.active == elem+1)[0]
                print(f"Right neighbor is element {elem+1}")
            else:
                # Periodic case - last element's right neighbor is the first element
                right_active_idx = np.where(self.solver.active == 1)[0]
                print(f"Periodic right neighbor: connecting element {elem} to first element")
                
            if len(right_active_idx) > 0:
                right_idx = right_active_idx[0]
                right_nodes = self.solver.intma[:, right_idx]
                right_sol = self.solver.q[right_nodes]
                print(f"Right neighbor solution values: {right_sol}")
                
                # Calculate jump at right interface
                local_jumps[-1] = abs(elem_right - right_sol[0])
                neighbor_jumps[1] = local_jumps[-1]
                print(f"Right interface jump: {local_jumps[-1]:.6f}")
                        
            # ====== Calculate Interior Jumps ======
            print("Calculating interior jumps...")
            for i in range(1, self.solver.ngl-1):
                local_jumps[i] = abs(elem_sol[i] - elem_sol[i-1])
                print(f"Interior jump {i}: {local_jumps[i]:.6f}")
                    
        except Exception as e:
            print(f"Error in _get_element_jumps: {e}")
            print(f"Element index: {element_idx}, Active elements: {len(self.solver.active)}")
            print(f"Stack trace:")
            import traceback
            traceback.print_exc()
            return np.zeros(self.solver.ngl), np.zeros(2)
        
        print("\nFinal jump values:")
        print(f"Local jumps: {local_jumps}")
        print(f"Neighbor jumps: {neighbor_jumps}")
                
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
        local_jumps, neighbor_jumps = self._get_element_jumps(self.current_element)

        
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
        element_nodes = self.solver.intma[:, self.current_element]
        solution_values = self.solver.q[element_nodes]


        # Add debug prints before return
        print("\nObservation debug:")
        print(f"Local jumps: {local_jumps}")
        print(f"Neighbor jumps: {neighbor_jumps}") 
        print(f"Solution values: {self.solver.q[self.solver.intma[:, self.current_element]]}")
    
        
        return {
            'local_jumps': local_jumps.astype(np.float32),
            'neighbor_jumps': neighbor_jumps.astype(np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }


    def calculate_resource_penalty(self, new_resources):
        """Calculate penalty for resource usage"""
        if new_resources >= 1.0:
            return 1000.0
            # return float('inf')  # or a very large number like 1e6
        elif new_resources <= 0.0:
            return 0.0
        else:
            return self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)


    def _compute_reward(self, delta_u: float, new_resources: float) -> float:
        """
        Compute reward following paper's formulation.
        
        Reward = accuracy_term - resource_penalty where:
        - accuracy_term = log(|Δu| + ε) - log(ε)
        - resource_penalty = γc * sqrt(p)/(1-p)
        
        Args:
            delta_u: Change in solution after adaptation
            new_resources: New resource usage fraction
            
        Returns:
            float: Computed reward value
        """
        # Accuracy reward (log of solution change)
        accuracy = np.log(abs(delta_u) + self.machine_eps) - np.log(self.machine_eps)
        
        # Resource penalty using barrier function
        # resource_penalty = self.gamma_c * np.sqrt(new_resources) / (1 - new_resources)

                # Add this before calculating resource_penalty
        if new_resources > 0.9:  # you can adjust this threshold
            print(f"WARNING: High resource usage detected: {new_resources:.3f}")
            print(f"Current element: {self.current_element}")
            print(f"Number of active elements: {len(self.solver.active)}")
            
        resource_penalty = self.calculate_resource_penalty(new_resources)

        print("\nReward debug:")
        print(f"delta_u: {delta_u}")
        print(f"accuracy term: {accuracy}")
        print(f"resource penalty: {resource_penalty}")
        print(f"final reward: {accuracy - resource_penalty}")
        
        return float(accuracy - resource_penalty)
        


    def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
        """
        Execute one step of the environment.
        
        Process:
        1. Store current state
        2. Apply AMR action to current element
        3. Take solver timestep
        4. Compute reward based on solution change and resource usage
        5. Get new observation
        6. Select next element randomly
        
        Args:
            action: Element adaptation (0=coarsen, 1=no change, 2=refine)
                
        Returns:
            tuple: (observation, reward, terminated, truncated, info)
                observation: New environment state
                reward: Reward for action taken  
                terminated: Whether episode naturally ended (always False)
                truncated: Whether resources exceeded
                info: Additional diagnostics
        """
        print(f"\nStep debug:")
        print(f"Current element: {self.current_element}")
        print(f"Active elements: {len(self.solver.active)}")
        print(f"Action: {action}")

        # Store initial state
        old_solution = self.solver.q.copy()
        old_grid = self.solver.coord.copy()
        old_active = self.solver.active.copy()
        old_resources = len(self.solver.active)
                    
        # SAFETY CHECK: Ensure current_element is valid
        if self.current_element >= len(self.solver.active):
            self.current_element = len(self.solver.active) - 1
            print(f"Corrected current element to: {self.current_element}")

        # Apply AMR action to current element  
        marks_override = {self.current_element: action - 1}  # Convert to {-1, 0, 1}
        
        try:
            # adapt_mesh will handle budget checks internally
            self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
        except ValueError as e:
            # Balance enforcement would exceed budget
            print(f"Adaptation failed: {e}")
            return self._get_observation(), -1000.0, False, False, {
                'delta_u': 0.0,
                'resource_usage': old_resources / self.element_budget,
                'n_elements': old_resources,
                'budget_exceeded': True,
                'error': str(e)
            }

        self.current_element = min(self.current_element, len(self.solver.active) - 1)
        
        print(f"After adapt_mesh:")
        print(f"New active elements: {len(self.solver.active)}")
        
        # Take solver timestep
        self.solver.step()
        
        # Get new state
        new_solution = self.solver.q
        new_grid = self.solver.coord
        new_resources = len(self.solver.active)

        # Check if budget exceeded (this shouldn't happen due to adapt_mesh checks, but just in case)
        budget_exceeded = new_resources > self.element_budget
        
        if budget_exceeded:
            # Revert to previous state
            self.solver.q = old_solution
            self.solver.coord = old_grid
            self.solver.active = old_active
            reward = -1000.0  # Large penalty
            # During training, we continue the episode
            truncated = False  # Changed from True
            delta_u = 0.0
        else:
            # Compare solutions on appropriate grid
            if len(new_solution) >= len(old_solution):
                old_interpolated = np.interp(new_grid, old_grid, old_solution)
                delta_u = np.linalg.norm(new_solution - old_interpolated)
            else:
                new_interpolated = np.interp(old_grid, new_grid, new_solution)
                delta_u = np.linalg.norm(new_interpolated - old_solution)

            # Compute reward using normal reward function
            reward = self._compute_reward(delta_u, new_resources / self.element_budget)
            truncated = False

        # Get observation of new state
        observation = self._get_observation()
        
        # Always false as episodes don't end naturally
        terminated = False
        
        # Collect diagnostic information
        info = {
            'delta_u': delta_u,
            'resource_usage': new_resources / self.element_budget,
            'n_elements': new_resources,
            'budget_exceeded': budget_exceeded
        }
        
        # Randomly select next element if continuing
        if not truncated:
            n_active = len(self.solver.active)
            if n_active > 0:
                new_current = np.random.randint(0, n_active)
                print(f"Selected new element: {new_current} out of {n_active}")
                self.current_element = new_current
            else:
                print("Warning: No active elements!")
                self.current_element = 0

        return observation, reward, terminated, truncated, info
    # def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
    #     """
    #     Execute one step of the environment.
        
    #     Process:
    #     1. Store current state
    #     2. Apply AMR action to current element
    #     3. Take solver timestep
    #     4. Compute reward based on solution change and resource usage
    #     5. Get new observation
    #     6. Select next element randomly
        
    #     Args:
    #         action: Element adaptation (0=coarsen, 1=no change, 2=refine)
                
    #     Returns:
    #         tuple: (observation, reward, terminated, truncated, info)
    #             observation: New environment state
    #             reward: Reward for action taken  
    #             terminated: Whether episode naturally ended (always False)
    #             truncated: Whether resources exceeded
    #             info: Additional diagnostics
    #     """
    #     print(f"\nStep debug:")
    #     print(f"Current element: {self.current_element}")
    #     print(f"Active elements: {len(self.solver.active)}")
    #     print(f"Action: {action}")

    #     # Store initial state
    #     old_solution = self.solver.q.copy()
    #     old_grid = self.solver.coord.copy()
    #     old_active = self.solver.active.copy()
    #     old_resources = len(self.solver.active)
        
    #     # SAFETY CHECK: Ensure current_element is valid
    #     if self.current_element >= len(self.solver.active):
    #         self.current_element = len(self.solver.active) - 1
    #         print(f"Corrected current element to: {self.current_element}")

    #     # Pre-check budget for refinement action
    #     if action == 2:  # refine
    #         potential_new_elements = old_resources + 1
    #         if potential_new_elements > self.element_budget:
    #             # Return early with penalty but don't truncate episode
    #             print(f"Refinement rejected: would exceed budget ({potential_new_elements} > {self.element_budget})")
    #             return self._get_observation(), -100.0, False, False, {
    #                 'delta_u': 0.0,
    #                 'resource_usage': old_resources / self.element_budget,
    #                 'n_elements': old_resources,
    #                 'budget_exceeded': True
    #             }

    #     # Apply AMR action with budget constraint
    #     marks_override = {self.current_element: action - 1}  # Convert to {-1, 0, 1}
    #     try:
    #         self.solver.adapt_mesh(marks_override=marks_override, element_budget=self.element_budget)
    #     except Exception as e:
    #         print(f"Error in adapt_mesh: {e}")
    #         # Revert to previous state
    #         self.solver.q = old_solution
    #         self.solver.coord = old_grid
    #         self.solver.active = old_active
    #         return self._get_observation(), -100.0, False, False, {
    #             'delta_u': 0.0,
    #             'resource_usage': old_resources / self.element_budget,
    #             'n_elements': old_resources,
    #             'error': str(e)
    #         }

    #     # Update current element index if mesh changed
    #     self.current_element = min(self.current_element, len(self.solver.active) - 1)
        
    #     print(f"After adapt_mesh:")
    #     print(f"New active elements: {len(self.solver.active)}")
        
    #     # Take solver timestep
    #     self.solver.step()
        
    #     # Get new state
    #     new_solution = self.solver.q
    #     new_grid = self.solver.coord
    #     new_resources = len(self.solver.active)

    #     # Post-check budget (in case balance enforcement added elements)
    #     budget_exceeded = new_resources > self.element_budget
        
    #     if budget_exceeded:
    #         # Revert to previous state
    #         self.solver.q = old_solution
    #         self.solver.coord = old_grid
    #         self.solver.active = old_active
    #         reward = -1000.0  # Large penalty
    #         truncated = True
    #         delta_u = 0.0
    #     else:
    #         # Compare solutions on appropriate grid
    #         if len(new_solution) >= len(old_solution):
    #             old_interpolated = np.interp(new_grid, old_grid, old_solution)
    #             delta_u = np.linalg.norm(new_solution - old_interpolated)
    #         else:
    #             new_interpolated = np.interp(old_grid, new_grid, new_solution)
    #             delta_u = np.linalg.norm(new_interpolated - old_solution)

    #         # Compute reward using normal reward function
    #         reward = self._compute_reward(delta_u, new_resources / self.element_budget)
    #         truncated = False

    #     # Get observation of new state
    #     observation = self._get_observation()
        
    #     # Episodes don't end naturally
    #     terminated = False
        
    #     # Collect diagnostic information
    #     info = {
    #         'delta_u': delta_u,
    #         'resource_usage': new_resources / self.element_budget,
    #         'n_elements': new_resources,
    #         'budget_exceeded': budget_exceeded
    #     }
        
    #     # Randomly select next element if continuing
    #     if not truncated:
    #         n_active = len(self.solver.active)
    #         if n_active > 0:
    #             new_current = np.random.randint(0, n_active)
    #             print(f"Selected new element: {new_current} out of {n_active}")
    #             self.current_element = new_current
    #         else:
    #             print("Warning: No active elements!")
    #             self.current_element = 0
        
    #     return observation, reward, terminated, truncated, info
    
    
    # def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
    #     """
    #     Execute one step of the environment.
        
    #     Process:
    #     1. Store current state
    #     2. Apply AMR action to current element
    #     3. Take solver timestep
    #     4. Compute reward based on solution change and resource usage
    #     5. Get new observation
    #     6. Select next element randomly
        
    #     Args:
    #         action: Element adaptation (0=coarsen, 1=no change, 2=refine)
                
    #     Returns:
    #         tuple: (observation, reward, terminated, truncated, info)
    #             observation: New environment state
    #             reward: Reward for action taken  
    #             terminated: Whether episode naturally ended (always False)
    #             truncated: Whether resources exceeded
    #             info: Additional diagnostics
    #     """
    #     # Store initial state
    #     old_solution = self.solver.q.copy()
    #     old_grid = self.solver.coord.copy()
    #     old_resources = len(self.solver.active) / self.solver.max_elements

    #     # Apply AMR action to current element  
    #     marks_override = {self.current_element: action - 1}  # Convert to {-1, 0, 1}
    #     self.solver.adapt_mesh(marks_override=marks_override)
        
    #     # Take solver timestep
    #     self.solver.step()
        
    #     # Get new state
    #     new_solution = self.solver.q
    #     new_grid = self.solver.coord
    #     new_resources = len(self.solver.active) / self.solver.max_elements

    #     # Check if budget exceeded
    #     budget_exceeded = len(self.solver.active) > self.solver.max_elements

    #     if budget_exceeded:
    #         # Apply large negative reward and end episode
    #         reward = -1000.0  # Large penalty
    #         truncated = True
    #         delta_u = 0.0
    #     else:
    #         # Compare solutions
    #         if len(new_solution) >= len(old_solution):
    #             old_interpolated = np.interp(new_grid, old_grid, old_solution)
    #             delta_u = np.linalg.norm(new_solution - old_interpolated)
    #         else:
    #             new_interpolated = np.interp(old_grid, new_grid, new_solution)
    #             delta_u = np.linalg.norm(new_interpolated - old_solution)

    #         # Compute reward using normal reward function
    #         reward = self._compute_reward(delta_u, new_resources)
    #         truncated = False

    #     # Get observation of new state
    #     observation = self._get_observation()
        
    #     # Always false as episodes don't end naturally
    #     terminated = False
        
    #     # Collect diagnostic information
    #     info = {
    #         'delta_u': delta_u,
    #         'resource_usage': new_resources,
    #         'n_elements': len(self.solver.active),
    #         'budget_exceeded': budget_exceeded
    #     }
        
    #     # Randomly select next element if continuing
    #     if not truncated:
    #         self.current_element = np.random.randint(0, len(self.solver.active))
        
    #     return observation, reward, terminated, truncated, info


    # def step(self, action: int) -> Tuple[Dict[str, np.ndarray], float, bool, bool, Dict[str, Any]]:
    #     """
    #     Execute one step of the environment.
        
    #     Process:
    #     1. Store current state
    #     2. Apply AMR action to current element
    #     3. Take solver timestep
    #     4. Compute reward based on solution change and resources
    #     5. Get new observation
    #     6. Select next element randomly
        
    #     Args:
    #         action: Element adaptation (0=coarsen, 1=no change, 2=refine)
            
    #     Returns:
    #         tuple: (observation, reward, terminated, truncated, info)
    #     """
    #     # Store initial state
    #     old_solution = self.solver.q.copy()
    #     old_grid = self.solver.coord.copy()  # Store old grid
    #     old_resources = len(self.solver.active) / self.solver.max_elements
        
    #     # Apply AMR action to current element
    #     marks_override = {self.current_element: action - 1}  # Convert to {-1, 0, 1}
    #     self.solver.adapt_mesh(marks_override=marks_override)
        
    #     # Take solver timestep
    #     self.solver.step()
        
    #     # Get new solution
    #     new_solution = self.solver.q
    #     new_grid = self.solver.coord
        
    #     # Compute change in solution by interpolating to finer grid
    #     if len(new_solution) >= len(old_solution):
    #         # Interpolate old solution to new grid
    #         old_interpolated = np.interp(new_grid, old_grid, old_solution)
    #         delta_u = np.linalg.norm(new_solution - old_interpolated)
    #     else:
    #         # Interpolate new solution to old grid
    #         new_interpolated = np.interp(old_grid, new_grid, new_solution)
    #         delta_u = np.linalg.norm(new_interpolated - old_solution)
        
    #     # Get new resource usage
    #     new_resources = len(self.solver.active) / self.solver.max_elements
        
    #     # Compute reward
    #     reward = self._compute_reward(delta_u, new_resources)
        
    #     # Get new observation
    #     observation = self._get_observation()
        
    #     # Check termination
    #     terminated = False
    #     truncated = (new_resources >= 1.0)
        
    #     # Additional info for debugging
    #     info = {
    #         'delta_u': delta_u,
    #         'resource_usage': new_resources,
    #         'n_elements': len(self.solver.active)
    #     }
        
    #     # Move to next element randomly
    #     self.current_element = np.random.randint(0, len(self.solver.active))
        
    #     return observation, reward, terminated, truncated, info
        # # Store initial state
        # old_solution = self.solver.q.copy()
        # old_resources = len(self.solver.active) / self.solver.max_elements
        
        # # Apply AMR action to current element
        # marks_override = {self.current_element: action - 1}  # Convert to {-1, 0, 1}
        # self.solver.adapt_mesh(criterion = 1, marks_override=marks_override)
            
        # # Take solver timestep
        # self.solver.step()
        
        # # Compute change in solution
        # new_solution = self.solver.q
        # delta_u = np.linalg.norm(new_solution - old_solution)
        
        # # Get new resource usage
        # new_resources = len(self.solver.active) / self.solver.max_elements
        
        # # Compute reward
        # reward = self._compute_reward(delta_u, new_resources)
        
        # # Get new observation
        # observation = self._get_observation()
        
        # # Check termination
        # terminated = False  # Episode doesn't naturally terminate
        # truncated = (new_resources >= 1.0)  # Truncate if resources exceeded
        
        # # Additional info for debugging
        # info = {
        #     'delta_u': delta_u,
        #     'resource_usage': new_resources,
        #     'n_elements': len(self.solver.active)
        # }
        
        # # Randomly select next element
        # self.current_element = np.random.randint(0, len(self.solver.active))
        
        # return observation, reward, terminated, truncated, info


    
    # def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    #     """
    #     Reset environment to initial state.
        
    #     Args:
    #         seed: Random seed for reproducibility
    #         options: Additional options (unused)
            
    #     Returns:
    #         tuple: (observation, info)
    #     """
    #     super().reset(seed=seed)
        
    #     # Reset solver
    #     self.solver.reset()
        
    #     # Start with random element
    #     self.current_element = np.random.randint(0, len(self.solver.active))
        
    #     return self._get_observation(), {}
    
    def reset(self, seed=None, options=None) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
        """
        Reset environment with mesh quality checks and recovery strategies.
        
        Args:
            seed: Random seed
            options: Additional options
            
        Returns:
            tuple: (observation, info)
        """
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
                'n_elements': len(element_sizes)
            }
        }
        
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