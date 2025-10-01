#!/usr/bin/env python3
"""
Automatically generate CODESTRUCTURE.md from current directory structure.
"""

import os
import sys
from pathlib import Path

def should_ignore(path_name):
    """Check if a directory or file should be ignored."""
    ignore_patterns = {
        # Directories
        '__pycache__', '.git', '.pytest_cache', '.vscode', '.idea',
        'node_modules', '.env', 'venv', 'env', '.conda',
        # Files
        '.DS_Store', '*.pyc', '*.pyo', '*.pyd', '.gitignore',
        # Results and logs (optional - you might want to include these)
        # 'logs', 'experiments/results'
    }
    
    return any(pattern in str(path_name) or path_name.name.startswith('.') 
               for pattern in ignore_patterns)

def generate_tree(root_path, prefix="", max_depth=None, current_depth=0):
    """Generate tree structure recursively."""
    if max_depth and current_depth >= max_depth:
        return []
    
    items = []
    root = Path(root_path)
    
    # Get all items, sort directories first, then files
    try:
        all_items = list(root.iterdir())
        dirs = [item for item in all_items if item.is_dir() and not should_ignore(item)]
        files = [item for item in all_items if item.is_file() and not should_ignore(item)]
        
        # Sort both lists
        dirs.sort(key=lambda x: x.name.lower())
        files.sort(key=lambda x: x.name.lower())
        
        all_sorted = dirs + files
        
        for i, item in enumerate(all_sorted):
            is_last = i == len(all_sorted) - 1
            
            # Choose the right prefix
            current_prefix = "└── " if is_last else "├── "
            next_prefix = "    " if is_last else "│   "
            
            # Add current item
            items.append(f"{prefix}{current_prefix}{item.name}")
            
            # Recurse into directories
            if item.is_dir():
                sub_items = generate_tree(
                    item, 
                    prefix + next_prefix, 
                    max_depth, 
                    current_depth + 1
                )
                items.extend(sub_items)
                
    except PermissionError:
        items.append(f"{prefix}[Permission Denied]")
    
    return items

def main():
    """Main function to generate code structure."""
    # Get project root (current directory)
    project_root = Path.cwd()
    project_name = project_root.name
    
    # Generate the tree
    print(f"Generating code structure for {project_name}...")
    tree_lines = [f"{project_name}/"]
    tree_lines.extend(generate_tree(project_root, max_depth=4))  # Limit depth
    
    # Create header
    header = [
        "# Project Code Structure",
        "",
        f"Auto-generated on: {os.popen('date').read().strip()}",
        f"Project: {project_name}",
        "",
        "```",
    ]
    
    footer = [
        "```",
        "",
        "## Key Directories",
        "",
        "- **experiments/**: Training configurations and results",
        "- **numerical/**: Core AMR and RL implementation",
        "- **slurm_scripts/**: HPC job submission scripts", 
        "- **logs/**: SLURM job output and error logs",
        "- **tools/**: Utility scripts and analysis tools",
        "",
        "*Generated automatically using tools/generate_codestructure.py*"
    ]
    
    # Write to file
    output_file = "LOCAL_CODESTRUCTURE.md"
    with open(output_file, 'w') as f:
        f.write('\n'.join(header + tree_lines + footer))
    
    print(f"Code structure written to {output_file}")
    print(f"Lines generated: {len(tree_lines)}")

if __name__ == "__main__":
    main()
