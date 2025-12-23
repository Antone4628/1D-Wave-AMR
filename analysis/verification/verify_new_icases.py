#!/usr/bin/env python3
"""
Verification script for new exact_solution() test cases (icase 10, 11, 12).

Location: analysis/verification/verify_new_icases.py

Purpose:
    - Verify new initial conditions are implemented correctly
    - Check periodicity at domain boundaries
    - Visualize time evolution
    - Run BEFORE deploying models on new test cases

Usage (from project root):
    python analysis/verification/verify_new_icases.py
    
    Or with VS Code terminal in project root:
    python analysis/verification/verify_new_icases.py

Output:
    - Prints periodicity check results
    - Saves verification plot to analysis/verification/verify_new_icases.png
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add project root to path (assumes script is in analysis/verification/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

from numerical.solvers.utils import exact_solution

def main():
    print("=" * 60)
    print("Verification: New exact_solution() test cases")
    print("=" * 60)
    
    # Test domain
    x = np.linspace(-1, 1, 500)
    npoin = len(x)
    
    # Define test cases
    cases = [
        (1, 'Gaussian (training)', 'tab:gray'),
        (10, 'tanh', 'tab:blue'),
        (11, 'erf', 'tab:orange'),
        (12, 'sigmoid', 'tab:green'),
    ]
    
    # ================================================================
    # Test 1: Periodicity check at t=0
    # ================================================================
    print("\n[Test 1] Periodicity check at t=0:")
    print("-" * 40)
    all_periodic = True
    for icase, name, _ in cases:
        qe, u = exact_solution(x, npoin, 0.0, icase)
        diff = abs(qe[0] - qe[-1])
        status = "✓ PASS" if diff < 1e-10 else "✗ FAIL"
        if diff >= 1e-10:
            all_periodic = False
        print(f"  icase={icase:2d} ({name:20s}): u(-1)={qe[0]:+.6f}, u(1)={qe[-1]:+.6f}, diff={diff:.2e} {status}")
    
    # ================================================================
    # Test 2: Wave speed check
    # ================================================================
    print("\n[Test 2] Wave speed check:")
    print("-" * 40)
    for icase, name, _ in cases:
        _, u = exact_solution(x, npoin, 0.0, icase)
        expected = 2.0
        status = "✓ PASS" if abs(u - expected) < 1e-10 else "✗ FAIL"
        print(f"  icase={icase:2d} ({name:20s}): wave_speed={u}, expected={expected} {status}")
    
    # ================================================================
    # Test 3: Time evolution visualization
    # ================================================================
    print("\n[Test 3] Generating time evolution plots...")
    print("-" * 40)
    
    fig, axes = plt.subplots(4, 3, figsize=(14, 12))
    times = [0.0, 0.25, 0.5]
    
    for row, (icase, name, color) in enumerate(cases):
        for col, t in enumerate(times):
            ax = axes[row, col]
            qe, u = exact_solution(x, npoin, t, icase)
            ax.plot(x, qe, color=color, linewidth=2)
            ax.set_title(f'icase={icase} ({name}), t={t}', fontsize=10)
            ax.set_xlabel('x', fontsize=9)
            ax.set_ylabel('u', fontsize=9)
            ax.grid(True, alpha=0.3)
            ax.set_xlim(-1, 1)
            
            # Set y-limits based on case
            if icase == 1:
                ax.set_ylim(-0.1, 1.1)
            else:
                ax.set_ylim(-1.3, 1.3)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axhline(y=1, color='k', linewidth=0.5, linestyle='--', alpha=0.3)
                ax.axhline(y=-1, color='k', linewidth=0.5, linestyle='--', alpha=0.3)
    
    fig.suptitle('Exact Solution Verification: Time Evolution\n' +
                 'Wave should advect right by Δx = c×Δt = 2×0.25 = 0.5 per column',
                 fontsize=12)
    plt.tight_layout()
    
    # Save to same directory as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'verify_new_icases.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"  Saved: {output_path}")
    
    # ================================================================
    # Test 4: Advection distance check
    # ================================================================
    print("\n[Test 4] Advection distance check (t=0 to t=0.25):")
    print("-" * 40)
    print("  Expected shift: Δx = c×Δt = 2.0 × 0.25 = 0.5")
    
    for icase, name, _ in cases[1:]:  # Skip Gaussian (different structure)
        qe_t0, _ = exact_solution(x, npoin, 0.0, icase)
        qe_t025, _ = exact_solution(x, npoin, 0.25, icase)
        
        # Find zero crossing at t=0 (should be near x=0)
        zero_idx_t0 = np.argmin(np.abs(qe_t0))
        zero_x_t0 = x[zero_idx_t0]
        
        # Find zero crossing at t=0.25 (should be near x=0.5)
        zero_idx_t025 = np.argmin(np.abs(qe_t025))
        zero_x_t025 = x[zero_idx_t025]
        
        shift = zero_x_t025 - zero_x_t0
        expected_shift = 0.5
        status = "✓ PASS" if abs(shift - expected_shift) < 0.01 else "✗ FAIL"
        print(f"  icase={icase:2d} ({name:20s}): zero crossing moved from x={zero_x_t0:.3f} to x={zero_x_t025:.3f}, shift={shift:.3f} {status}")
    
    # ================================================================
    # Summary
    # ================================================================
    print("\n" + "=" * 60)
    print("Verification complete!")
    print("=" * 60)
    print("\nIf all tests pass, the new icases are ready for model evaluation.")
    print("Run models with: --icase 10, --icase 11, or --icase 12")
    

if __name__ == "__main__":
    main()