"""
Sequential ModelMarker for Adaptive Mesh Refinement

This implementation follows a sequential vs. batch approach by:
1. Sorting elements by non-conformity (jump magnitude)
2. Processing elements sequentially
3. Updating the mesh after each element decision
4. Recomputing the solution after each adaptation
5. Tracking resource usage accurately
"""

import numpy as np
from stable_baselines3 import A2C  # Or whichever algorithm you trained with

class ModelMarkerSequential:
    """
    Uses a trained RL model to mark elements for adaptive mesh refinement.
    
    This class implements the sequential marking functionality following Foucart's approach.
    Elements are processed in order of their non-conformity, with the mesh and solution 
    updated after each decision.
    """
    
    def __init__(self, model_path, solver, element_budget=None, verbose=False):
        """
        Initialize the sequential model marker.
        
        Args:
            model_path: Path to the trained RL model
            solver: Instance of DGWaveSolver to access mesh and solution data
            element_budget: Maximum number of elements allowed (defaults to solver.max_elements)
            verbose: Whether to print detailed logs
        """
        self.solver = solver
        self.element_budget = element_budget or solver.max_elements
        self.verbose = verbose
        
        # Load the trained model
        self.model = A2C.load(model_path)
        
        # Action mapping consistent with training
        self.action_mapping = {
            0: -1,  # coarsen
            1: 0,   # do nothing
            2: 1    # refine
        }
    
    def get_element_jumps(self, element_idx):
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
                print(f"Warning: Invalid element index {element_idx}")
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
                print(f"Error in get_element_jumps: {e}")
            return np.zeros(self.solver.ngl), np.zeros(2)
                
        return local_jumps, neighbor_jumps
    
    def compute_element_non_conformity(self, element_idx):
        """
        Compute the non-conformity measure (ϵK) for an element.
        
        This is the key metric for sorting elements in Foucart's approach.
        
        Args:
            element_idx: Index of element in active list
            
        Returns:
            float: Non-conformity measure (integral of jump magnitudes)
        """
        local_jumps, _ = self.get_element_jumps(element_idx)
        
        # Sum of jumps as a simple approximation of the integral of |[uh]|
        non_conformity = np.sum(local_jumps)
        
        return non_conformity
    
    def get_observation(self, element_idx):
        """
        Get observation for an element in the format expected by the model.
        
        Args:
            element_idx: Index of element in active_grid
                
        Returns:
            dict: Observation dictionary compatible with the trained model
        """
        # Get local solution jumps
        local_jumps, _ = self.get_element_jumps(element_idx)
        
        # Calculate average of local jumps for this element
        avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        avg_local_jump = 0.0 if np.isnan(avg_local_jump) else avg_local_jump
        
        # Compute average jump across all elements
        all_jumps = []
        for i in range(len(self.solver.active)):
            jumps, _ = self.get_element_jumps(i)
            if not np.any(np.isnan(jumps)):
                all_jumps.append(np.mean(jumps))
        
        avg_jump = np.mean(all_jumps) if all_jumps else 0.0
        avg_jump = 0.0 if np.isnan(avg_jump) else avg_jump
        
        # Current resource usage
        resource_usage = len(self.solver.active) / self.element_budget
        
        # Get local solution values
        element_nodes = self.solver.intma[:, element_idx]
        solution_values = self.solver.q[element_nodes]
        solution_values = np.nan_to_num(solution_values)
        
        observation = {
            'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
            'avg_jump': np.array([avg_jump], dtype=np.float32),
            'resource_usage': np.array([resource_usage], dtype=np.float32),
            'solution_values': solution_values.astype(np.float32)
        }
        
        return observation
    
    def is_action_valid(self, element_idx, action):
        """
        Check if the requested action is valid for the given element.
        
        Args:
            element_idx: Index of element in active list
            action: Action to check (-1: coarsen, 0: do nothing, 1: refine)
            
        Returns:
            bool: True if action is valid, False otherwise
        """
        # Do-nothing action is always valid
        if action == 0:
            return True
        
        # Resource check for refinement
        if action == 1:
            if len(self.solver.active) >= self.element_budget:
                if self.verbose:
                    print(f"Refinement not possible: would exceed budget")
                return False
            
            # Get element and its current level
            elem = self.solver.active[element_idx]
            current_level = self.solver.label_mat[elem-1][4]  # Level is stored in column 4
            
            # Check if already at max level
            if current_level >= self.solver.max_level:
                if self.verbose:
                    print(f"Element {elem} already at max level")
                return False
            
            return True
        
        # Coarsening check
        elif action == -1:
            elem = self.solver.active[element_idx]
            
            # Get element level
            current_level = self.solver.label_mat[elem-1][4]
            
            # Can't coarsen level 0 elements
            if current_level == 0:
                if self.verbose:
                    print(f"Element {elem} at level 0 can't be coarsened")
                return False
            
            # Check for parent
            parent = self.solver.label_mat[elem-1][1]
            if parent == 0:
                if self.verbose:
                    print(f"Element {elem} has no parent, can't coarsen")
                return False
            
            # Find sibling
            sibling = None
            
            # Check element before current one
            if elem > 1 and elem-1 in self.solver.active:
                potential_sibling = elem-1
                if self.solver.label_mat[potential_sibling-1][1] == parent:
                    sibling = potential_sibling
            
            # Check element after current one
            if sibling is None and elem < len(self.solver.label_mat) and elem+1 in self.solver.active:
                potential_sibling = elem+1
                if self.solver.label_mat[potential_sibling-1][1] == parent:
                    sibling = potential_sibling
            
            # Need sibling to coarsen
            if sibling is None:
                if self.verbose:
                    print(f"No sibling found for element {elem}, can't coarsen")
                return False
            
            return True
        
        # Should never reach here with valid action values
        return False
    
    def apply_action(self, element_idx, action_int):
        """
        Apply the action to the element and update mesh and solution.
        
        Args:
            element_idx: Index of element in active list
            action_int: Action index from the model (0, 1, or 2)
            
        Returns:
            bool: Whether the action was successfully applied
        """
        # Map the action to a mark
        mapped_action = self.action_mapping[action_int]
        
        # Check if action is valid
        if not self.is_action_valid(element_idx, mapped_action):
            if self.verbose:
                print(f"Invalid action {mapped_action} for element {element_idx}, defaulting to do nothing")
            return False
        
        # Special handling for coarsening
        if mapped_action == -1:
            elem = self.solver.active[element_idx]
            parent = self.solver.label_mat[elem-1][1]
            
            # Find sibling
            sibling = None
            sibling_idx = None
            
            # Check element before current one
            if elem > 1:
                potential_sibling = elem-1
                if potential_sibling in self.solver.active and self.solver.label_mat[potential_sibling-1][1] == parent:
                    sibling = potential_sibling
                    sibling_idx = np.where(self.solver.active == sibling)[0][0]
            
            # Check element after current one
            if sibling is None and elem < len(self.solver.label_mat):
                potential_sibling = elem+1
                if potential_sibling in self.solver.active and self.solver.label_mat[potential_sibling-1][1] == parent:
                    sibling = potential_sibling
                    sibling_idx = np.where(self.solver.active == sibling)[0][0]
            
            # Create marks for coarsening both elements
            if sibling is not None:
                marks = np.zeros(len(self.solver.active), dtype=int)
                marks[element_idx] = -1
                marks[sibling_idx] = -1
                
                if self.verbose:
                    print(f"Coarsening elements {elem} and {sibling}")
            else:
                # Shouldn't reach here as is_action_valid should have checked
                if self.verbose:
                    print(f"No sibling found for element {elem}, skipping coarsening")
                return False
        else:
            # For refinement or do-nothing, just mark the current element
            marks = np.zeros(len(self.solver.active), dtype=int)
            marks[element_idx] = mapped_action
            
            if self.verbose and mapped_action == 1:
                print(f"Refining element {self.solver.active[element_idx]}")
        
        # Apply the adaptation to the mesh
        try:
            old_elements = len(self.solver.active)
            
            # Adapt the mesh with the specified marks
            self.solver.adapt_mesh(
                marks=marks,
                element_budget=self.element_budget,
                balance=None,  # Use solver's default
                update_dt=False  # Don't update time step yet
            )
            
            # Recompute the steady-state solution
            improved_steady_solution = self.solver.steady_solve_improved()
            self.solver.q = improved_steady_solution
            
            new_elements = len(self.solver.active)
            
            if self.verbose:
                print(f"Elements changed from {old_elements} to {new_elements}")
            
            return True
            
        except Exception as e:
            if self.verbose:
                print(f"Error applying action: {e}")
            return False
    
    def mark_and_adapt_sequentially(self):
        """
        Mark and adapt elements sequentially following Foucart's approach.
        
        This method:
        1. Computes non-conformity for all elements
        2. Sorts elements by non-conformity (largest first)
        3. Processes elements sequentially, updating the mesh after each action
        
        Returns:
            int: Number of elements successfully adapted
        """
        # Display initial state
        if self.verbose:
            print(f"Initial active elements: {len(self.solver.active)}/{self.element_budget}")
            print(f"Initial resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
        # Calculate non-conformity for each element
        n_active_initial = len(self.solver.active)
        non_conformities = []
        
        for idx in range(n_active_initial):
            non_conformity = self.compute_element_non_conformity(idx)
            non_conformities.append((idx, non_conformity))
        
        # Sort by non-conformity in descending order
        sorted_elements = sorted(non_conformities, key=lambda x: x[1], reverse=True)
        
        if self.verbose:
            print(f"Sorted {len(sorted_elements)} elements by non-conformity")
            for i, (idx, non_conf) in enumerate(sorted_elements[:5]):
                if i < 5:  # Just show top 5
                    print(f"  Element {self.solver.active[idx]}: non-conformity = {non_conf:.6f}")
        
        # Track how many elements are successfully adapted
        successful_adaptations = 0
        
        # Process each element in sorted order
        for original_idx, non_conformity in sorted_elements:
            # After an adaptation, the element indices will change
            # We need to recalculate which element is currently at the original position
            
            # Skip if we've reached the element budget
            if len(self.solver.active) >= self.element_budget and successful_adaptations > 0:
                if self.verbose:
                    print(f"Reached element budget ({self.element_budget}), stopping adaptation")
                break
            
            # Find the current position of this element (which may have changed due to previous adaptations)
            try:
                # This is a simplified approach - in reality, you may need more sophisticated tracking
                # of elements between adaptations
                if original_idx >= len(self.solver.active):
                    if self.verbose:
                        print(f"Element index {original_idx} now out of bounds, skipping")
                    continue
                
                # Get current observation
                observation = self.get_observation(original_idx)
                
                # Query the model for an action
                action, _ = self.model.predict(observation, deterministic=True)
                
                # Convert to int for mapping
                action_int = int(action.item()) if hasattr(action, 'item') else int(action)
                
                # Apply the action
                success = self.apply_action(original_idx, action_int)
                
                if success:
                    successful_adaptations += 1
                    if self.verbose:
                        print(f"Successfully adapted element {original_idx}, action={self.action_mapping[action_int]}")
                        print(f"Current resource usage: {len(self.solver.active)/self.element_budget:.2f}")
                
            except Exception as e:
                if self.verbose:
                    print(f"Error processing element {original_idx}: {e}")
                continue
        
        # Update time step after all adaptations
        self.solver._compute_timestep(use_actual_max_level=True)
        
        if self.verbose:
            print(f"Sequential adaptation complete: {successful_adaptations} elements adapted")
            print(f"Final active elements: {len(self.solver.active)}/{self.element_budget}")
            print(f"Final resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
        return successful_adaptations