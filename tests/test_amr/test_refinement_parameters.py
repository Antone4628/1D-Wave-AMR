#!/usr/bin/env python
"""
Test script for verifying proper parameter flow from YAML config to solver initialization,
specifically for mesh refinement parameters.
"""

import os
import sys
import yaml
import unittest
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Add project root to path to allow importing from project
PROJECT_ROOT = str(Path(__file__).resolve().parents[2])
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed
from numerical.amr.forest import forest


class TestRefinementParameters(unittest.TestCase):
    """Test class for verifying refinement parameter flow from config to initialization."""
    
    def setUp(self):
        """Set up test environment."""
        # Base solver parameters
        self.nop = 4
        self.xelem = np.array([-1, -0.4, 0, 0.4, 1])
        self.max_elements = 50
        self.max_level = 8
        self.courant_max = 0.1
        self.icase = 1
        self.verbose = False
        
        # Create test configs directory if it doesn't exist
        self.test_config_dir = os.path.join(PROJECT_ROOT, "tests", "test_amr", "test_configs")
        os.makedirs(self.test_config_dir, exist_ok=True)
        
        # Create output directory for visualizations
        self.output_dir = os.path.join(PROJECT_ROOT, "tests", "test_amr", "visualizations")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Define colors for different refinement levels
        self.level_colors = {
            0: 'blue',
            1: 'green',
            2: 'orange',
            3: 'red',
            4: 'purple',
            5: 'brown',
            6: 'pink',
            7: 'cyan',
            8: 'magenta'
        }
        
    def create_test_config(self, filename, refinement_config):
        """Create a test YAML config file with specific refinement settings."""
        config = {
            "environment": {
                "max_episode_steps": 200,
                "element_budget": 25,
                "gamma_c": 50.0,
                "rl_iterations_per_timestep": "random",
                "max_rl_iterations": 100,
                "max_consecutive_no_action": 100,
                "step_domain_fraction": 0.125,
                "initial_refinement": refinement_config
            },
            "solver": {
                "nop": 4,
                "max_level": 8,
                "courant_max": 0.1,
                "icase": 1,
                "initial_elements": [-1, -0.4, 0, 0.4, 1],
                "verbose": False,
                "balance": True
            }
        }
        
        config_path = os.path.join(self.test_config_dir, filename)
        with open(config_path, 'w') as f:
            yaml.dump(config, f)
        
        return config_path
    
    def load_config(self, config_path):
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Convert initial_elements to numpy array if present
        if 'solver' in config and 'initial_elements' in config['solver']:
            config['solver']['initial_elements'] = np.array(config['solver']['initial_elements'])
        
        return config
    
    def get_refinement_options(self, config):
        """Extract refinement options from config."""
        refinement_options = {}
        refinement_config = config.get('environment', {}).get('initial_refinement', {})
        
        refinement_options['refinement_mode'] = refinement_config.get('mode', 'none')
        refinement_options['refinement_level'] = refinement_config.get('fixed_level', 0)
        refinement_options['refinement_max_level'] = refinement_config.get('max_initial_level', 3)
        refinement_options['refinement_probability'] = refinement_config.get('probability', 0.5)
        
        return refinement_options
    
    def count_elements_by_level(self, solver):
        """Count active elements by refinement level."""
        level_counts = {}
        
        for elem in solver.active:
            level = solver.label_mat[elem-1][4]  # Level is stored in column 4
            level_counts[level] = level_counts.get(level, 0) + 1
            
        return level_counts
    
    def visualize_mesh(self, solver, title, filename):
        """Create a visualization of the mesh with color-coded refinement levels."""
        # Get active elements and their levels
        active_elements = solver.active
        active_levels = solver.get_active_levels()
        
        # Create figure
        plt.figure(figsize=(12, 6))
        ax = plt.subplot(111)
        
        # Plot each element with appropriate color for its level
        for i, (elem_num, level) in enumerate(zip(active_elements, active_levels)):
            # Element numbers are 1-based, so subtract 1
            elem_idx = elem_num - 1
            
            # Get coordinates from info_mat
            left_coord = solver.info_mat[elem_idx, 1]
            right_coord = solver.info_mat[elem_idx, 2]
            
            width = right_coord - left_coord
            color = self.level_colors.get(level, 'gray')
            
            # Plot element as rectangle
            rect = plt.Rectangle((left_coord, 0), width, 0.5, 
                               facecolor=color, alpha=0.7, edgecolor='black')
            ax.add_patch(rect)
            
            # Add element number and level as text
            plt.text(left_coord + width/2, 0.25, f"{elem_num}\nL{level}", 
                   ha='center', va='center', color='white', fontweight='bold')
        
        # Set plot limits and labels
        plt.xlim(-1.1, 1.1)
        plt.ylim(-0.1, 0.6)
        plt.title(title)
        plt.xlabel('Domain Coordinate')
        
        # Create legend for refinement levels
        legend_elements = [plt.Rectangle((0, 0), 1, 1, facecolor=self.level_colors.get(level, 'gray'), 
                                       alpha=0.7, edgecolor='black', label=f'Level {level}') 
                         for level in sorted(set(active_levels))]
        
        plt.legend(handles=legend_elements, loc='upper right')
        
        # Save the figure
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()
        
        print(f"Visualization saved as {filename}")
        
    def visualize_element_distribution(self, solver, title, filename):
        """Create a bar chart showing the distribution of elements by refinement level."""
        # Get level counts
        level_counts = self.count_elements_by_level(solver)
        
        # Create bar chart
        plt.figure(figsize=(10, 6))
        levels = sorted(level_counts.keys())
        counts = [level_counts[level] for level in levels]
        
        bars = plt.bar(levels, counts, color=[self.level_colors.get(level, 'gray') for level in levels])
        
        # Add count labels on top of bars
        for bar, count in zip(bars, counts):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, 
                    str(count), ha='center', va='bottom')
        
        plt.title(title)
        plt.xlabel('Refinement Level')
        plt.ylabel('Number of Elements')
        plt.xticks(levels)
        plt.ylim(0, max(counts) * 1.2)  # Add some space for labels
        
        # Save the figure
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()
        
        print(f"Element distribution chart saved as {filename}")
    
    def test_fixed_refinement(self):
        """Test fixed refinement parameter flow."""
        # Create test config with fixed refinement
        refinement_config = {
            "mode": "fixed",
            "fixed_level": 2,
            "max_initial_level": 3,
            "probability": 0.7
        }
        
        config_path = self.create_test_config("test_fixed_refinement.yaml", refinement_config)
        config = self.load_config(config_path)
        refinement_options = self.get_refinement_options(config)
        
        # Initialize solver with refinement options
        solver = DGWaveSolverMixed(
            nop=self.nop,
            xelem=self.xelem,
            max_elements=self.max_elements,
            max_level=self.max_level,
            courant_max=self.courant_max,
            icase=self.icase,
            verbose=self.verbose
        )
        
        # Apply refinement via reset method
        solver.reset(**refinement_options)
        
        # Get level counts and verify all elements are at the specified level
        level_counts = self.count_elements_by_level(solver)
        
        print(f"Fixed refinement test - Level counts: {level_counts}")
        # In fixed mode at level 2, all elements should be at level 2
        self.assertTrue(2 in level_counts, "No elements at level 2")
        self.assertEqual(sum(level_counts.values()), len(solver.active), 
                         "Level count sum doesn't match active elements count")
        
        # Additional check - no elements should be at level 0 in fixed refinement level 2
        self.assertFalse(0 in level_counts, "Level 0 elements found in fixed level 2 refinement")
        
        # Create visualizations
        self.visualize_mesh(solver, 
                          f"Fixed Refinement (Level {refinement_options['refinement_level']})", 
                          "fixed_refinement_mesh.png")
        self.visualize_element_distribution(solver, 
                                         f"Element Distribution for Fixed Refinement (Level {refinement_options['refinement_level']})", 
                                         "fixed_refinement_distribution.png")
    
    def test_random_refinement(self):
        """Test random refinement parameter flow."""
        # Create test config with random refinement
        refinement_config = {
            "mode": "random",
            "fixed_level": 1,
            "max_initial_level": 3,
            "probability": 1.0  # Set to 1.0 to guarantee refinement
        }
        
        config_path = self.create_test_config("test_random_refinement.yaml", refinement_config)
        config = self.load_config(config_path)
        refinement_options = self.get_refinement_options(config)
        
        # Initialize solver with refinement options
        solver = DGWaveSolverMixed(
            nop=self.nop,
            xelem=self.xelem,
            max_elements=self.max_elements,
            max_level=self.max_level,
            courant_max=self.courant_max,
            icase=self.icase,
            verbose=self.verbose
        )
        
        # Apply refinement via reset method
        solver.reset(**refinement_options)
        
        # Get level counts
        level_counts = self.count_elements_by_level(solver)
        print(f"Random refinement test - Level counts: {level_counts}")
        
        # In random mode with probability 1.0 up to max_initial_level 3, 
        # we should have elements up to level 3
        has_higher_levels = any(level > 0 for level in level_counts.keys())
        self.assertTrue(has_higher_levels, "No refinement performed in random mode")
        
        # Ensure max level doesn't exceed max_initial_level
        self.assertTrue(max(level_counts.keys()) <= refinement_options['refinement_max_level'], 
                        f"Refinement exceeds max_initial_level of {refinement_options['refinement_max_level']}")
        
        # Create visualizations
        self.visualize_mesh(solver, 
                          f"Random Refinement (Max Level {refinement_options['refinement_max_level']}, Prob {refinement_options['refinement_probability']})", 
                          "random_refinement_mesh.png")
        self.visualize_element_distribution(solver, 
                                         f"Element Distribution for Random Refinement", 
                                         "random_refinement_distribution.png")
    
    def test_no_refinement(self):
        """Test no refinement mode."""
        # Create test config with no refinement
        refinement_config = {
            "mode": "none",
            "fixed_level": 2,
            "max_initial_level": 3,
            "probability": 0.7
        }
        
        config_path = self.create_test_config("test_no_refinement.yaml", refinement_config)
        config = self.load_config(config_path)
        refinement_options = self.get_refinement_options(config)
        
        # Initialize solver with refinement options
        solver = DGWaveSolverMixed(
            nop=self.nop,
            xelem=self.xelem,
            max_elements=self.max_elements,
            max_level=self.max_level,
            courant_max=self.courant_max,
            icase=self.icase,
            verbose=self.verbose
        )
        
        # Apply refinement via reset method
        solver.reset(**refinement_options)
        
        # Get level counts
        level_counts = self.count_elements_by_level(solver)
        print(f"No refinement test - Level counts: {level_counts}")
        
        # In no refinement mode, all elements should be at level 0
        self.assertEqual(list(level_counts.keys()), [0], 
                         f"Expected only level 0 elements, got levels: {list(level_counts.keys())}")
        self.assertEqual(level_counts.get(0, 0), len(solver.active), 
                         "Not all elements are at level 0")
        
        # Create visualizations
        self.visualize_mesh(solver, "No Refinement (Initial Mesh)", "no_refinement_mesh.png")
        self.visualize_element_distribution(solver, "Element Distribution for No Refinement", 
                                         "no_refinement_distribution.png")

    def test_edge_case_low_levels(self):
        """Test edge case with refinement_level=0 but refinement_max_level>0."""
        # This tests the robustness of the conditional in the reset method
        refinement_config = {
            "mode": "random",
            "fixed_level": 0,  # This is 0, which would fail with the old condition
            "max_initial_level": 2,  # But this is >0, which should allow refinement
            "probability": 1.0  # Set to 1.0 to guarantee refinement
        }
        
        config_path = self.create_test_config("test_edge_case.yaml", refinement_config)
        config = self.load_config(config_path)
        refinement_options = self.get_refinement_options(config)
        
        # Initialize solver with refinement options
        solver = DGWaveSolverMixed(
            nop=self.nop,
            xelem=self.xelem,
            max_elements=self.max_elements,
            max_level=self.max_level,
            courant_max=self.courant_max,
            icase=self.icase,
            verbose=self.verbose
        )
        
        # Apply refinement via reset method
        solver.reset(**refinement_options)
        
        # Get level counts
        level_counts = self.count_elements_by_level(solver)
        print(f"Edge case test - Level counts: {level_counts}")
        
        # Should have refinement even though refinement_level=0
        has_higher_levels = any(level > 0 for level in level_counts.keys())
        self.assertTrue(has_higher_levels, 
                        "No refinement performed in random mode with refinement_level=0 and refinement_max_level>0")
        
        # Create visualizations
        self.visualize_mesh(solver, 
                          f"Edge Case (fixed_level=0, max_level={refinement_options['refinement_max_level']})", 
                          "edge_case_mesh.png")
        self.visualize_element_distribution(solver, 
                                         "Element Distribution for Edge Case", 
                                         "edge_case_distribution.png")

    def test_comparison_visualizations(self):
        """Create a side-by-side comparison of all refinement methods."""
        # Initialize all the configs we want to test
        configs = [
            {
                "name": "No Refinement",
                "mode": "none",
                "fixed_level": 0,
                "max_initial_level": 0,
                "probability": 0.0
            },
            {
                "name": "Fixed Level 1",
                "mode": "fixed",
                "fixed_level": 1,
                "max_initial_level": 3,
                "probability": 0.7
            },
            {
                "name": "Fixed Level 2",
                "mode": "fixed",
                "fixed_level": 2,
                "max_initial_level": 3,
                "probability": 0.7
            },
            {
                "name": "Random (Max Level 2)",
                "mode": "random",
                "fixed_level": 0,
                "max_initial_level": 2,
                "probability": 0.7
            },
            {
                "name": "Random (Max Level 3)",
                "mode": "random",
                "fixed_level": 0,
                "max_initial_level": 3,
                "probability": 0.7
            }
        ]
        
        # Create solvers with each configuration
        solvers = []
        for config in configs:
            solver = DGWaveSolverMixed(
                nop=self.nop,
                xelem=self.xelem,
                max_elements=self.max_elements,
                max_level=self.max_level,
                courant_max=self.courant_max,
                icase=self.icase,
                verbose=self.verbose
            )
            
            # Apply refinement
            solver.reset(
                refinement_mode=config["mode"],
                refinement_level=config["fixed_level"],
                refinement_max_level=config["max_initial_level"],
                refinement_probability=config["probability"]
            )
            
            solvers.append((config["name"], solver))
        
        # Create a comparison visualization for mesh
        self.create_mesh_comparison(solvers, "refinement_comparison_mesh.png")
        
        # Create a comparison visualization for element distributions
        self.create_distribution_comparison(solvers, "refinement_comparison_distribution.png")
        
        # Assert that we have different refinement patterns
        level_distributions = [self.count_elements_by_level(solver) for _, solver in solvers]
        
        # All level distributions should not be identical
        are_all_same = all(d == level_distributions[0] for d in level_distributions)
        self.assertFalse(are_all_same, "All refinement methods produced identical meshes")
        
    def create_mesh_comparison(self, solvers, filename):
        """Create a side-by-side comparison of meshes."""
        n_configs = len(solvers)
        fig, axes = plt.subplots(n_configs, 1, figsize=(12, 4 * n_configs), squeeze=False)
        
        for i, (name, solver) in enumerate(solvers):
            ax = axes[i, 0]
            
            # Get active elements and levels
            active_elements = solver.active
            active_levels = solver.get_active_levels()
            
            # Plot elements
            for j, (elem_num, level) in enumerate(zip(active_elements, active_levels)):
                # Element numbers are 1-based, so subtract 1
                elem_idx = elem_num - 1
                
                # Get coordinates from info_mat
                left_coord = solver.info_mat[elem_idx, 1]
                right_coord = solver.info_mat[elem_idx, 2]
                
                width = right_coord - left_coord
                color = self.level_colors.get(level, 'gray')
                
                rect = plt.Rectangle((left_coord, 0), width, 0.5, 
                                    facecolor=color, alpha=0.7, edgecolor='black',
                                    transform=ax.transData)
                ax.add_patch(rect)
                
                # Add element index and level as text if there's enough space
                if width > 0.05:  # Only add text for elements that are wide enough
                    ax.text(left_coord + width/2, 0.25, f"{elem_num}\nL{level}", 
                            ha='center', va='center', color='white', fontweight='bold')
            
            # Set limits and labels
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-0.1, 0.6)
            ax.set_title(f"{name} - {len(active_elements)} Elements")
            
            # Add a text summary of level counts
            level_counts = self.count_elements_by_level(solver)
            level_summary = ", ".join([f"L{k}: {v}" for k, v in sorted(level_counts.items())])
            ax.text(-1.0, -0.05, level_summary, fontsize=9, ha='left')
            
            # Only show x-label on the bottom plot
            if i == n_configs - 1:
                ax.set_xlabel('Domain Coordinate')
                
        # Create a common legend
        legend_elements = []
        all_levels = set()
        for _, solver in solvers:
            all_levels.update(solver.get_active_levels())
        
        for level in sorted(all_levels):
            legend_elements.append(
                plt.Rectangle((0, 0), 1, 1, facecolor=self.level_colors.get(level, 'gray'), 
                            alpha=0.7, edgecolor='black', label=f'Level {level}')
            )
        
        fig.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.95, 0.98))
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()
        
        print(f"Mesh comparison visualization saved as {filename}")
    
    def create_distribution_comparison(self, solvers, filename):
        """Create a comparison of element distributions."""
        # Calculate the maximum number of levels across all solvers
        max_level = 0
        for _, solver in solvers:
            level_counts = self.count_elements_by_level(solver)
            if level_counts:
                max_level = max(max_level, max(level_counts.keys()))
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Set width of bars
        bar_width = 0.15
        index = np.arange(max_level + 1)
        
        # Plot bars for each solver
        for i, (name, solver) in enumerate(solvers):
            level_counts = self.count_elements_by_level(solver)
            counts = [level_counts.get(level, 0) for level in range(max_level + 1)]
            
            position = index + (i - len(solvers)/2 + 0.5) * bar_width
            bars = ax.bar(position, counts, bar_width, 
                        label=name, 
                        color=[self.level_colors.get(level, 'gray') for level in range(max_level + 1)])
            
            # Add count labels
            for bar, count in zip(bars, counts):
                if count > 0:  # Only add label for non-zero counts
                    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3, 
                            str(count), ha='center', va='bottom', fontsize=8)
        
        # Add labels and legend
        ax.set_xlabel('Refinement Level')
        ax.set_ylabel('Number of Elements')
        ax.set_title('Element Distribution by Refinement Level')
        ax.set_xticks(index)
        ax.set_xticklabels([f'Level {i}' for i in range(max_level + 1)])
        ax.legend()
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close()
        
        print(f"Distribution comparison visualization saved as {filename}")


def run_single_test():
    """Run a single test for quick validation."""
    # Create a test instance
    test = TestRefinementParameters()
    test.setUp()
    
    # Run the comparison test to generate all visualizations
    print("Running comparison visualizations test...")
    test.test_comparison_visualizations()
    
    print("Test completed. Check the visualizations directory for output images.")


def run_all_tests():
    """Run all test methods for comprehensive testing."""
    # Create a test instance
    test = TestRefinementParameters()
    test.setUp()
    
    print("\n--- RUNNING ALL REFINEMENT PARAMETER TESTS ---\n")
    
    print("\n1. Running fixed refinement test...")
    test.test_fixed_refinement()
    
    print("\n2. Running random refinement test...")
    test.test_random_refinement()
    
    print("\n3. Running no refinement test...")
    test.test_no_refinement()
    
    print("\n4. Running edge case test...")
    test.test_edge_case_low_levels()
    
    print("\n5. Running comparison visualizations test...")
    test.test_comparison_visualizations()
    
    print("\n--- ALL TESTS COMPLETED ---")
    print("Check the visualizations directory for output images.")


if __name__ == "__main__":
    print("Script is running...")
    
    # Change this to run_all_tests() if you want to run all tests
    run_single_test()