import numpy as np
import os
from stable_baselines3 import A2C  # Or whichever algorithm you trained with

class ModelMarker:
    """
    Uses a trained RL model to mark elements for adaptive mesh refinement.
    
    This class implements the marking functionality using a trained RL model
    to decide which elements should be refined, coarsened, or left unchanged.
    """
    
    def __init__(self, model_path, solver, element_budget=None, verbose=False):
        """
        Initialize the model marker.
        
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
    
    def get_observation(self, element_idx):
        """
        Get observation for an element in the format expected by the model.
        
        Args:
            element_idx: Index of element in active_grid
                
        Returns:
            dict: Observation dictionary compatible with the trained model
        """
        # Get local solution jumps
        local_jumps, _ = self._get_element_jumps(element_idx)
        
        # Calculate average of local jumps for this element
        avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
        avg_local_jump = 0.0 if np.isnan(avg_local_jump) else avg_local_jump
        
        # Compute average jump across all elements
        all_jumps = []
        for i in range(len(self.solver.active)):
            jumps, _ = self._get_element_jumps(i)
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
    
    def _get_element_jumps(self, element_idx):
        """
        Compute solution jumps at element boundaries and interior nodes.
        
        This is implemented as in the DGAMREnv class.
        
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
                print(f"Error in _get_element_jumps: {e}")
            return np.zeros(self.solver.ngl), np.zeros(2)
                
        return local_jumps, neighbor_jumps

    def mark(self, active_grid, label_mat, intma, q, criterion=None):
        """
        Mark elements for refinement/coarsening based on the trained model.
        
        Args:
            active_grid: Currently active element indices
            label_mat: Element family relationships [rows, 4]
            intma: Element-node connectivity
            q: Solution values
            criterion: Not used, kept for API compatibility
            
        Returns:
            marks: Element markers (-1:derefine, 0:no change, 1:refine)
        """
        n_active = len(active_grid)
        marks = np.zeros(n_active, dtype=int)
        
        # Current resource usage
        resource_usage = len(active_grid) / self.element_budget
        
        # Process each active element
        for idx in range(n_active):
            # Get observation for this element
            observation = self.get_observation(idx)
            
            # Query the model for an action
            action, _ = self.model.predict(observation, deterministic=True)

            # Convert numpy array to int for dictionary lookup
            action_int = int(action.item()) if hasattr(action, 'item') else int(action)         
            
            # Map the action to a mark
            mark_value = self.action_mapping[action_int]
            
            # Apply budget constraints - can't refine if at max elements
            if mark_value == 1 and resource_usage >= 1.0:
                mark_value = 0
                
            # Handle coarsening case - ensures sibling is also marked
            if mark_value == -1:
                elem = active_grid[idx]
                parent = label_mat[elem-1][1]
                
                # Only proceed if element has a parent
                if parent != 0:
                    # Find sibling
                    sibling = None
                    sibling_idx = None
                    
                    # Check element before current one
                    if elem > 1 and idx > 0 and label_mat[elem-2][1] == parent:
                        sibling = elem - 1
                        sibling_idx = idx - 1
                        
                    # Check element after current one
                    elif elem < len(label_mat) and idx < n_active-1 and label_mat[elem][1] == parent:
                        sibling = elem + 1
                        sibling_idx = idx + 1
                    
                    # Check if sibling is valid for coarsening
                    if sibling is not None and sibling in active_grid:
                        if self.verbose:
                            print(f"Marking element {elem} and sibling {sibling} for coarsening")
                        marks[idx] = -1
                        marks[sibling_idx] = -1
                    else:
                        # No valid sibling, can't coarsen
                        if self.verbose:
                            print(f"No valid sibling for element {elem}, can't coarsen")
                        mark_value = 0
            
            # Set the mark value
            marks[idx] = mark_value
            
        return marks