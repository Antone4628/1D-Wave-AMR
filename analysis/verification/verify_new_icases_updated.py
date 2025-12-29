#!/usr/bin/env python3
"""
Verification script for new exact_solution() test cases (icase 10-16).

Location: analysis/verification/verify_new_icases.py

Purpose:
    - Verify new initial conditions are implemented correctly
    - Check periodicity at domain boundaries
    - Visualize time evolution
    - Run BEFORE deploying models on new test cases

Usage (from project root):
    python analysis/verification/verify_new_icases.py
    
Output:
    - Prints verification results to console
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
    print("=" * 70)
    print("Verification: New exact_solution() test cases (icases 10-16)")
    print("=" * 70)
    
    # Test domain
    x = np.linspace(-1, 1, 500)
    npoin = len(x)
    
    # Define all test cases
    cases = [
        # Baseline
        (1, 'Gaussian (training)', 'tab:gray'),
        # Smooth square waves (icases 10-12)
        (10, 'tanh', 'tab:blue'),
        (11, 'erf', 'tab:orange'),
        (12, 'sigmoid', 'tab:green'),
        # Additional test functions (icases 13-16)
        (13, 'Multi-Gaussian', 'tab:purple'),
        (14, 'Bump (compact)', 'tab:brown'),
        (15, 'Sech² (soliton)', 'tab:pink'),
        (16, 'Mexican Hat', 'tab:red'),
    ]
    
    # ================================================================
    # Test 1: Periodicity check at t=0
    # ================================================================
    print("\n[Test 1] Periodicity check at t=0:")
    print("-" * 50)
    all_pass = True
    for icase, name, _ in cases:
        qe, u = exact_solution(x, npoin, 0.0, icase)
        diff = abs(qe[0] - qe[-1])
        status = "✓ PASS" if diff < 1e-6 else "✗ FAIL"
        if diff >= 1e-6:
            all_pass = False
        print(f"  icase={icase:2d} ({name:20s}): u(-1)={qe[0]:+.6f}, u(1)={qe[-1]:+.6f}, diff={diff:.2e} {status}")
    
    # ================================================================
    # Test 2: Wave speed check
    # ================================================================
    print("\n[Test 2] Wave speed check:")
    print("-" * 50)
    for icase, name, _ in cases:
        _, u = exact_solution(x, npoin, 0.0, icase)
        expected = 2.0
        status = "✓ PASS" if abs(u - expected) < 1e-10 else "✗ FAIL"
        if abs(u - expected) >= 1e-10:
            all_pass = False
        print(f"  icase={icase:2d} ({name:20s}): wave_speed={u}, expected={expected} {status}")
    
    # ================================================================
    # Test 3: Time evolution visualization
    # ================================================================
    print("\n[Test 3] Generating time evolution plots...")
    print("-" * 50)
    
    fig, axes = plt.subplots(8, 3, figsize=(14, 20))
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
            
            # Dynamic y-limits based on icase
            if icase == 1:  # Gaussian
                ax.set_ylim(-0.1, 1.2)
            elif icase in [10, 11, 12]:  # Smooth square waves
                ax.set_ylim(-1.3, 1.3)
                ax.axhline(y=0, color='k', linewidth=0.5)
            elif icase == 16:  # Mexican hat has negative values
                ax.set_ylim(-0.5, 1.2)
                ax.axhline(y=0, color='k', linewidth=0.5)
            else:  # icases 13, 14, 15
                ax.set_ylim(-0.1, 1.2)
    
    fig.suptitle('Exact Solution Verification: All New Test Cases (icases 10-16)\n' +
                 'Wave should advect right by Δx = c×Δt = 2×0.25 = 0.5 per column',
                 fontsize=12)
    plt.tight_layout()
    
    # Save to same directory as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'verify_new_icases.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"  Saved: {output_path}")
    
    # ================================================================
    # Test 4: Advection distance check (t=0 to t=0.25)
    # ================================================================
    print("\n[Test 4] Advection distance check (t=0 to t=0.25):")
    print("-" * 50)
    print("  Expected shift: Δx = c×Δt = 2.0 × 0.25 = 0.5")
    print("  (Checking peak/feature location shift)")
    
    # Test cases with single peaks that are easy to track
    peak_cases = [
        (1, 'Gaussian (training)'),
        (14, 'Bump (compact)'),
        (15, 'Sech² (soliton)'),
        (16, 'Mexican Hat'),
    ]
    
    for icase, name in peak_cases:
        qe_t0, _ = exact_solution(x, npoin, 0.0, icase)
        qe_t025, _ = exact_solution(x, npoin, 0.25, icase)
        
        # Find peak location at t=0 and t=0.25
        peak_idx_t0 = np.argmax(qe_t0)
        peak_x_t0 = x[peak_idx_t0]
        
        peak_idx_t025 = np.argmax(qe_t025)
        peak_x_t025 = x[peak_idx_t025]
        
        shift = peak_x_t025 - peak_x_t0
        expected_shift = 0.5
        
        # Handle periodic wrapping
        if shift < -1.0:
            shift += 2.0
        
        status = "✓ PASS" if abs(shift - expected_shift) < 0.02 else "✗ FAIL"
        if abs(shift - expected_shift) >= 0.02:
            all_pass = False
        print(f"  icase={icase:2d} ({name:20s}): peak moved from x={peak_x_t0:.3f} to x={peak_x_t025:.3f}, shift={shift:.3f} {status}")
    
    # ================================================================
    # Test 5: Value range check
    # ================================================================
    print("\n[Test 5] Value range check at t=0:")
    print("-" * 50)
    for icase, name, _ in cases:
        qe, _ = exact_solution(x, npoin, 0.0, icase)
        min_val = np.min(qe)
        max_val = np.max(qe)
        
        # Expected ranges
        if icase in [10, 11, 12]:  # Smooth square waves: [-1, 1]
            expected_range = "[-1, 1]"
            range_ok = min_val >= -1.01 and max_val <= 1.01
        elif icase == 16:  # Mexican hat has negative values
            expected_range = "[-0.5, 1]"
            range_ok = min_val >= -0.6 and max_val <= 1.1
        else:  # Positive pulses: [0, 1] or [0, 2] for multi-Gaussian
            if icase == 13:
                expected_range = "[0, 2]"
                range_ok = min_val >= -0.01 and max_val <= 2.1
            else:
                expected_range = "[0, 1]"
                range_ok = min_val >= -0.01 and max_val <= 1.1
        
        status = "✓ PASS" if range_ok else "✗ FAIL"
        if not range_ok:
            all_pass = False
        print(f"  icase={icase:2d} ({name:20s}): min={min_val:+.4f}, max={max_val:+.4f}, expected {expected_range} {status}")
    
    # ================================================================
    # Summary
    # ================================================================
    print("\n" + "=" * 70)
    if all_pass:
        print("✓ ALL TESTS PASSED!")
    else:
        print("✗ SOME TESTS FAILED - Review output above")
    print("=" * 70)
    print("\nTest cases ready for model evaluation:")
    print("  icase=1:  Gaussian (training baseline)")
    print("  icase=10: tanh smooth square wave")
    print("  icase=11: erf smooth square wave")
    print("  icase=12: sigmoid smooth square wave")
    print("  icase=13: Multi-Gaussian (two pulses)")
    print("  icase=14: Bump function (compact support)")
    print("  icase=15: Sech² soliton profile")
    print("  icase=16: Mexican Hat (Ricker wavelet)")
    print("\nRun models with: --icase <number>")


if __name__ == "__main__":
    main()