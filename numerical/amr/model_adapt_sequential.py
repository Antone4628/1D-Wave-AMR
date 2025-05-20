"""
Sequential ModelMarker for Adaptive Mesh Refinement

This implementation follows a sequential sorted approach by:
1. Computing non-conformity for all elements
2. Processing the highest priority element
3. Recomputing priorities after each adaptation
4. Repeating until element budget is reached or no more adaptations needed
"""

import numpy as np
from stable_baselines3 import A2C  # Or whichever algorithm you trained with

class ModelMarkerSequential:
    """
    Uses a trained RL model to mark elements for adaptive mesh refinement.
    
    This class implements the sequential marking functionality following Foucart's approach.
    Elements are processed by priority, with the mesh and solution updated after each decision.
    Priorities are recomputed after each adaptation to ensure correct element selection.
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
    
    def compute_all_non_conformities(self):
        """
        Compute non-conformity measures for all elements in the current mesh.
        
        Returns:
            list: List of (element_idx, non_conformity) tuples sorted by non-conformity (highest first)
        """
        non_conformities = []
        
        for idx in range(len(self.solver.active)):
            non_conformity = self.compute_element_non_conformity(idx)
            non_conformities.append((idx, non_conformity))
            
        # Sort by non-conformity in descending order
        sorted_elements = sorted(non_conformities, key=lambda x: x[1], reverse=True)
        
        return sorted_elements
    
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
                    print(f"No valid sibling found for element {elem}, can't coarsen")
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
            bool: Whether the action was successfully applied and changed the mesh
        """
        # Map the action to a mark
        mapped_action = self.action_mapping[action_int]
        
        # Check if action is valid
        if not self.is_action_valid(element_idx, mapped_action):
            if self.verbose:
                print(f"Invalid action {mapped_action} for element {element_idx}, defaulting to do nothing")
            return False
        
        # No-op for do nothing
        if mapped_action == 0:
            if self.verbose:
                print(f"No action taken for element {self.solver.active[element_idx]}")
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
            # For refinement, just mark the current element
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
        
    def mark_and_adapt_single_round(self, max_adaptations=None):
        """
        Process a complete round of mesh adaptation with fixed element priorities.
        
        This method implements Foucart's approach with a crucial improvement to avoid
        oscillations: priorities are computed ONCE at the beginning of the round,
        and elements are processed in that fixed order, tracking elements by their
        unique element numbers rather than by indices.
        
        The method follows these steps:
        1. Compute non-conformity for all initial elements
        2. Sort elements by non-conformity (highest first)
        3. Process each element in priority order, checking if it still exists
        4. Complete when all initial elements have been processed
        
        Args:
            max_adaptations: Maximum number of adaptations to perform (optional)
            
        Returns:
            int: Number of elements successfully adapted
        """
        # Display initial state
        if self.verbose:
            print(f"Initial active elements: {len(self.solver.active)}/{self.element_budget}")
            print(f"Initial resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
        # Get initial active elements
        initial_active_elements = list(self.solver.active)
        
        # Compute non-conformity for all initial elements
        element_priorities = []
        for idx, elem_number in enumerate(initial_active_elements):
            non_conformity = self.compute_element_non_conformity(idx)
            element_priorities.append((elem_number, idx, non_conformity))
        
        # Sort by priority (highest non-conformity first)
        sorted_elements = sorted(element_priorities, key=lambda x: x[2], reverse=True)
        
        if self.verbose:
            print(f"Processing {len(sorted_elements)} elements in priority order")
            # Display top elements by priority
            for i, (elem, idx, non_conf) in enumerate(sorted_elements[:5]):
                if i < min(5, len(sorted_elements)):
                    print(f"  Priority #{i+1}: Element {elem} (non-conformity: {non_conf:.6f})")
        
        # Initialize tracking variables
        successful_adaptations = 0
        processed_elements = set()
        
        # Process each element in priority order
        for elem_number, original_idx, non_conformity in sorted_elements:
            # Check if we've hit the element budget
            if len(self.solver.active) >= self.element_budget:
                if self.verbose:
                    print(f"Reached element budget ({self.element_budget}), stopping adaptation")
                break
                    
            # Check if we've hit the max adaptations limit
            if max_adaptations is not None and successful_adaptations >= max_adaptations:
                if self.verbose:
                    print(f"Reached maximum adaptations limit ({max_adaptations})")
                break
                    
            # Skip elements with very low non-conformity
            if non_conformity < 1e-10:
                if self.verbose:
                    print(f"Element {elem_number} has non-conformity too low ({non_conformity:.6f}), skipping")
                continue
            
            # Skip if element no longer active (was already refined or coarsened)
            if elem_number not in self.solver.active:
                if self.verbose:
                    print(f"Element {elem_number} no longer active, skipping")
                continue
                
            # Find the current index of this element in the active list
            try:
                current_idx = np.where(self.solver.active == elem_number)[0][0]
            except IndexError:
                # This shouldn't happen given the check above, but just in case
                if self.verbose:
                    print(f"Element {elem_number} not found in active list, skipping")
                continue
            
            # Get observation for this element
            observation = self.get_observation(current_idx)
            
            # Query the model for an action
            action, _ = self.model.predict(observation, deterministic=True)
            
            # Convert to int for mapping
            action_int = int(action.item()) if hasattr(action, 'item') else int(action)
            mapped_action = self.action_mapping[action_int]
            
            # Skip do-nothing actions if we're just tracking them
            if mapped_action == 0:
                if self.verbose:
                    print(f"Element {elem_number}: no action (do nothing)")
                # Mark as processed even though no action taken
                processed_elements.add(elem_number)
                continue
            
            # Apply the action
            if self.verbose:
                print(f"Processing element {elem_number} (idx {current_idx}) with action {mapped_action}")
                    
            success = self.apply_action(current_idx, action_int)
            
            if success:
                successful_adaptations += 1
                if self.verbose:
                    print(f"Successfully adapted element {elem_number}, action={mapped_action}")
                    print(f"Current resource usage: {len(self.solver.active)/self.element_budget:.2f}")
            
            # Mark as processed (even if action failed)
            processed_elements.add(elem_number)
        
        # Update time step after all adaptations
        self.solver._compute_timestep(use_actual_max_level=True)
        
        if self.verbose:
            print(f"Adaptation round complete:")
            print(f"  Processed {len(processed_elements)}/{len(initial_active_elements)} initial elements")
            print(f"  Made {successful_adaptations} successful adaptations")
            print(f"  Final active elements: {len(self.solver.active)}/{self.element_budget}")
            print(f"  Final resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
        return successful_adaptations
    
    # def mark_and_adapt_sequentially(self, max_adaptations=None):
    #     """
    #     Mark and adapt elements following Foucart's sequential approach.
        
    #     This implementation properly handles mesh indexing changes by:
    #     1. Finding the highest priority element
    #     2. Processing just that element
    #     3. Recomputing priorities on the updated mesh
    #     4. Repeating until done
        
    #     Args:
    #         max_adaptations: Maximum number of adaptations to perform (optional)
            
    #     Returns:
    #         int: Number of elements successfully adapted
    #     """
    #     # Display initial state
    #     if self.verbose:
    #         print(f"Initial active elements: {len(self.solver.active)}/{self.element_budget}")
    #         print(f"Initial resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
    #     # Initialize adaptation counter
    #     successful_adaptations = 0
        
    #     # Track when to stop adapting
    #     keep_adapting = True
    #     consecutive_no_actions = 0
    #     max_consecutive_no_actions = 5  # Stop if we can't find any elements to adapt after 5 tries
        
    #     # Main adaptation loop
    #     while keep_adapting:
    #         # Check if we've hit the element budget
    #         if len(self.solver.active) >= self.element_budget:
    #             if self.verbose:
    #                 print(f"Reached element budget ({self.element_budget}), stopping adaptation")
    #             break
                
    #         # Check if we've hit the max adaptations limit
    #         if max_adaptations is not None and successful_adaptations >= max_adaptations:
    #             if self.verbose:
    #                 print(f"Reached maximum adaptations limit ({max_adaptations})")
    #             break
                
    #         # Compute non-conformity for all elements in the current mesh
    #         sorted_elements = self.compute_all_non_conformities()
            
    #         if self.verbose and sorted_elements:
    #             print(f"\nHighest non-conformity element: {self.solver.active[sorted_elements[0][0]]}, "
    #                   f"value: {sorted_elements[0][1]:.6f}")
            
    #         # Get the highest priority element
    #         if not sorted_elements:
    #             break
                
    #         best_idx, best_non_conformity = sorted_elements[0]
            
    #         # Skip elements with very low non-conformity
    #         if best_non_conformity < 1e-10:
    #             if self.verbose:
    #                 print(f"Highest non-conformity too low ({best_non_conformity:.6f}), stopping adaptation")
    #             break
            
    #         # Get observation for this element
    #         observation = self.get_observation(best_idx)
            
    #         # Query the model for an action
    #         action, _ = self.model.predict(observation, deterministic=True)
            
    #         # Convert to int for mapping
    #         action_int = int(action.item()) if hasattr(action, 'item') else int(action)
    #         mapped_action = self.action_mapping[action_int]
            
    #         # Apply the action
    #         if self.verbose:
    #             print(f"Processing element {self.solver.active[best_idx]} with action {mapped_action}")
                
    #         success = self.apply_action(best_idx, action_int)
            
    #         if success:
    #             successful_adaptations += 1
    #             consecutive_no_actions = 0
    #             if self.verbose:
    #                 print(f"Successfully adapted element, action={mapped_action}")
    #                 print(f"Current resource usage: {len(self.solver.active)/self.element_budget:.2f}")
    #         else:
    #             consecutive_no_actions += 1
    #             if self.verbose:
    #                 print(f"No adaptation made, consecutive failures: {consecutive_no_actions}")
                
    #         # Stop if we've had too many consecutive failures
    #         if consecutive_no_actions >= max_consecutive_no_actions:
    #             if self.verbose:
    #                 print(f"Too many consecutive failures ({consecutive_no_actions}), stopping adaptation")
    #             break
        
    #     # Update time step after all adaptations
    #     self.solver._compute_timestep(use_actual_max_level=True)
        
    #     if self.verbose:
    #         print(f"Sequential adaptation complete: {successful_adaptations} elements adapted")
    #         print(f"Final active elements: {len(self.solver.active)}/{self.element_budget}")
    #         print(f"Final resource usage: {len(self.solver.active)/self.element_budget:.2f}")
        
    #     return successful_adaptations