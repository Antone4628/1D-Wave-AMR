#!/usr/bin/env python3
"""
Test imports and path resolution for ANOVA analysis
"""

import sys
from pathlib import Path

print("🔍 Testing Import Paths")
print("=" * 50)

# Show current working directory
print(f"Current working directory: {Path.cwd()}")
print(f"Script location: {Path(__file__).resolve()}")

print("🔍 Testing Import Paths")
print("=" * 50)

# Show current working directory and script location
current_file = Path(__file__).resolve()
print(f"Current working directory: {Path.cwd()}")
print(f"Script location: {current_file}")

# Debug path resolution step by step
print(f"\nPath resolution debug:")
print(f"__file__: {Path(__file__)}")
print(f"Path(__file__).parent: {Path(__file__).parent}")
print(f"Path(__file__).parent.parent: {Path(__file__).parent.parent}")

# The analysis root should be /path/to/1D_wave_AMR/analysis/
analysis_root = Path(__file__).parent.parent  # This should be the analysis/ directory
print(f"Calculated analysis_root: {analysis_root.resolve()}")

# Add project paths using established pattern
sys.path.insert(0, str(analysis_root))
sys.path.insert(0, str(analysis_root / "data_management"))
sys.path.insert(0, str(analysis_root / "utilities"))

# Calculate paths
data_management_path = analysis_root / "data_management"
utilities_path = analysis_root / "utilities"

print(f"\nPath calculations:")
print(f"Analysis root: {analysis_root.resolve()}")
print(f"Data management path: {data_management_path.resolve()}")
print(f"Utilities path: {utilities_path.resolve()}")

# Check if paths exist
print(f"\nPath existence check:")
print(f"Data management exists: {data_management_path.exists()}")
print(f"Utilities exists: {utilities_path.exists()}")

if data_management_path.exists():
    data_loader_file = data_management_path / "data_loader.py"
    print(f"data_loader.py exists: {data_loader_file.exists()}")

if utilities_path.exists():
    config_file = utilities_path / "config.py"
    print(f"config.py exists: {config_file.exists()}")

# Test imports
print(f"\nTesting imports...")

try:
    from ..data_management.data_loader import quick_load_sweep
    print("✅ Successfully imported data_loader")
except ImportError as e:
    print(f"❌ Failed to import data_loader: {e}")

try:
    from ..utilities.config import CURRENT_SWEEP
    print("✅ Successfully imported config")
    print(f"   CURRENT_SWEEP: {CURRENT_SWEEP}")
except ImportError as e:
    print(f"❌ Failed to import config: {e}")

print(f"\nSys.path after modifications:")
for i, path in enumerate(sys.path[:5]):  # Show first 5 paths
    print(f"  {i}: {path}")