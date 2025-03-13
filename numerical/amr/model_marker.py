"""
RL-based Marker Module for Adaptive Mesh Refinement

This module provides a class for using trained RL models to make mesh refinement decisions
in the DG wave solver. It serves as an interface between the RL model and the existing
AMR framework.
"""

import numpy as np
from stable_baselines3 import PPO

class RLModelMarker:
    """
    Class for using trained RL models to make mesh refinement decisions.
    
    This class provides an interface compatible with the existing mark() function
    but uses a trained RL model to make decisions about which elements to refine
    or coarsen.
    
    Attributes:
        model: Loaded RL model (e.g., PPO)
        element_budget: Maximum allowed number of elements
        verbose: Whether to print detailed logs
        action_mapping: Maps model actions to refinement decisions
    """
    
    def __init__(self, model_path, element_budget, verbose=False):
        """
        Initialize the RL model-based marker.
        
        Args:
            model_path: Path to saved model (.zip file)
            element_budget: Maximum allowed number of elements
            verbose: Whether to print detailed logs
        """
        # Load the trained model
        self.model = PPO.load(model_path)  # Or whichever algorithm you used
        self.element_budget = element_budget
        self.verbose = verbose
        self.action_mapping = {0: -1, 1: 0, 2: 1}  # Map to {coarsen, no change, refine}
        
        # Monitoring statistics
        self.violation_count = 0
        self.decisions = {
            'refine': 0,
            'coarsen': 0,
            'no_change': 0
        }
        
    def calculate_observation(self, active_grid, label_mat, intma, q):
        """
        Calculate the observation for each element based on the current solution state.
        This should create the same observation format that your RL agent was trained with.
        
        Args:
            active_grid: Currently active element indices
            label_mat: Element family relationships
            intma: Element-node connectivity
            q: Current solution values
            
        Returns:
            list: Observations for each element in format expected by the RL model
        """
        observations = []
        
        for i, elem in enumerate(active_grid):
            # Get local solution jumps
            local_jumps, neighbor_jumps = self._get_element_jumps(i, active_grid, label_mat, intma, q)
            
            # Calculate average of local jumps for this element
            avg_local_jump = np.mean(local_jumps) if np.any(local_jumps) else 0.0
            
            # Compute average jump across all elements (similar to your env)
            all_jumps = []
            for j in range(len(active_grid)):
                jumps, _ = self._get_element_jumps(j, active_grid, label_mat, intma, q)
                if not np.any(np.isnan(jumps)):
                    all_jumps.append(np.mean(jumps))
            
            avg_jump = np.mean(all_jumps) if all_jumps else 0.0
            
            # Calculate jump ratio
            epsilon = 1e-10
            jump_ratio = avg_local_jump / (avg_jump + epsilon) if avg_jump > 0 else 1.0
            jump_ratio = min(jump_ratio, 10.0)  # Cap at 10.0
            
            # Resource usage
            resource_usage = len(active_grid) / self.element_budget
            
            # Get local solution values
            element_nodes = intma[:, i]
            solution_values = q[element_nodes]
            
            # Budget proximity features
            budget_proximity = resource_usage
            budget_headroom = self.element_budget - len(active_grid)
            refinement_safety = min(1.0, max(0.0, budget_headroom / 5.0))
            
            # Create observation dictionary matching your training format
            observations.append({
                'avg_local_jump': np.array([avg_local_jump], dtype=np.float32),
                'avg_jump': np.array([avg_jump], dtype=np.float32),
                'jump_ratio': np.array([jump_ratio], dtype=np.float32),
                'resource_usage': np.array([resource_usage], dtype=np.float32),
                'budget_proximity': np.array([budget_proximity], dtype=np.float32),
                'budget_headroom': np.array([budget_headroom], dtype=np.float32),
                'refinement_safety': np.array([refinement_safety], dtype=np.float32),
                'solution_values': solution_values.astype(np.float32)
            })
            
        return observations
    
    def _get_element_jumps(self, element_idx, active_grid, label_mat, intma, q):
        """
        Calculate solution jumps for an element.
        
        Args:
            element_idx: Index in active_grid
            active_grid: Currently active element indices
            label_mat: Element family relationships
            intma: Element-node connectivity
            q: Current solution values
            
        Returns:
            tuple: (local_jumps, neighbor_jumps)
        """
        # Get element number from active grid
        elem = active_grid[element_idx]
        
        # Extract solution values for current element
        elem_nodes = intma[:, element_idx]
        elem_sol = q[elem_nodes]
        
        # Get boundary values
        elem_left = elem_sol[0]
        elem_right = elem_sol[-1]
        
        # Initialize arrays for jumps
        local_jumps = np.zeros(len(elem_nodes))
        neighbor_jumps = np.zeros(2)
        
        try:
            # Handle Left Neighbor (with periodicity)
            if elem > 1:
                left_active_idx = np.where(active_grid == elem-1)[0]
            else:
                left_active_idx = np.where(active_grid == len(label_mat))[0]
                
            if len(left_active_idx) > 0:
                left_idx = left_active_idx[0]
                left_nodes = intma[:, left_idx]
                left_sol = q[left_nodes]
                
                # Calculate jump at left interface
                local_jumps[0] = abs(elem_left - left_sol[-1])
                neighbor_jumps[0] = local_jumps[0]
                        
            # Handle Right Neighbor (with periodicity)
            if elem < len(label_mat):
                right_active_idx = np.where(active_grid == elem+1)[0]
            else:
                right_active_idx = np.where(active_grid == 1)[0]
                
            if len(right_active_idx) > 0:
                right_idx = right_active_idx[0]
                right_nodes = intma[:, right_idx]
                right_sol = q[right_nodes]
                
                # Calculate jump at right interface
                local_jumps[-1] = abs(elem_right - right_sol[0])
                neighbor_jumps[1] = local_jumps[-1]
                        
            # Calculate Interior Jumps
            for i in range(1, len(elem_nodes)-1):
                local_jumps[i] = abs(elem_sol[i] - elem_sol[i-1])
                    
        except Exception as e:
            if self.verbose:
                print(f"Error in _get_element_jumps: {e}")
                import traceback
                traceback.print_exc()
            return np.zeros(len(elem_nodes)), np.zeros(2)
                
        return local_jumps, neighbor_jumps
    
    def __call__(self, active_grid, label_mat, intma, q, criterion=None):
        """
        Interface matching your existing mark() function.
        
        Args:
            active_grid: Currently active element indices
            label_mat: Element family relationships
            intma: Element-node connectivity
            q: Current solution values
            criterion: Ignored, included for compatibility
            
        Returns:
            marks (array): Element markers (-1:derefine, 0:no change, 1:refine)
        """
        # Check if we're already above budget (but don't modify decisions)
        current_elements = len(active_grid)
        if current_elements >= self.element_budget:
            self.violation_count += 1
            print(f"⚠️ BUDGET VIOLATION: {current_elements}/{self.element_budget} elements (violation #{self.violation_count})")
        elif current_elements >= self.element_budget * 0.9:
            print(f"⚠️ BUDGET WARNING: {current_elements}/{self.element_budget} elements (>90% utilized)")
        
        # Get observations for all elements
        observations = self.calculate_observation(active_grid, label_mat, intma, q)
        
        # Initialize marks
        marks = np.zeros(len(active_grid), dtype=int)
        
        # Tracking variables
        refine_count = 0
        coarsen_count = 0
        
        # Use model to predict action for each element
        for i, obs in enumerate(observations):
            action, _states = self.model.predict(obs, deterministic=True)
            # Convert numpy action to int for using as dictionary key
            if isinstance(action, np.ndarray):
                action = action.item()
            mapped_action = self.action_mapping[action]
            
            # Update metrics but don't override decisions
            if mapped_action == 1:  # Refine
                refine_count += 1
                self.decisions['refine'] += 1
            elif mapped_action == -1:  # Coarsen
                coarsen_count += 1
                self.decisions['coarsen'] += 1
            else:  # No change
                self.decisions['no_change'] += 1
                
            marks[i] = mapped_action
        
        # Log decision stats
        if self.verbose:
            print(f"RL model marked: {refine_count} refinements, {coarsen_count} coarsenings")
            print(f"Total decisions so far: {self.decisions}")
            
        return marks
    
    def get_statistics(self):
        """
        Return statistics about the RL model's decisions.
        
        Returns:
            dict: Statistics about model decisions and violations
        """
        return {
            'violations': self.violation_count,
            'decisions': self.decisions,
            'total_decisions': sum(self.decisions.values())
        }
    
    def reset_statistics(self):
        """Reset the monitoring statistics."""
        self.violation_count = 0
        self.decisions = {
            'refine': 0,
            'coarsen': 0,
            'no_change': 0
        }