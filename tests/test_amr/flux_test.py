import numpy as np
import matplotlib.pyplot as plt

import os
import sys
import traceback

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.dg.matrices import *
# from matrices import Fmatrix_rusanov_flux, Fmatrix_upwind_flux

def test_rusanov_flux():
    """Test the Rusanov flux matrix implementation."""
    # Create a simple test mesh
    nop = 2  # Polynomial order
    ngl = nop + 1  # Points per element
    nelem = 3  # Number of elements
    npoin = ngl * nelem  # Total points

    # Create simple connectivity matrix (each element has ngl points)
    intma = np.zeros((ngl, nelem), dtype=int)
    for e in range(nelem):
        for i in range(ngl):
            intma[i, e] = e * ngl + i

    # Print mesh structure
    print("Mesh Configuration:")
    print(f"  Elements: {nelem}, Points per element: {ngl}, Total points: {npoin}")
    print(f"  Connectivity matrix:\n{intma}")

    # Set wave speed
    wave_speed = 2.0
    
    # Create matrices
    F_rusanov = Fmatrix_rusanov_flux(intma, nelem, npoin, ngl, wave_speed, periodic=False)
    F_upwind = Fmatrix_upwind_flux(intma, nelem, npoin, ngl, wave_speed, periodic=False)
    
    # Verify specific matrix entries
    print("\nKey Matrix Entries:")
    print("  Left boundary (Rusanov):", F_rusanov[0, :3])
    print("  Left boundary (Upwind): ", F_upwind[0, :3])
    print("  Right boundary (Rusanov):", F_rusanov[-1, -3:])
    print("  Right boundary (Upwind): ", F_upwind[-1, -3:])
    
    # Verify interface treatment
    internal_interface1 = ngl - 1  # Right node of first element
    internal_interface2 = ngl      # Left node of second element
    print(f"\nInternal Interface Treatment at x={internal_interface1},{internal_interface2}:")
    print(f"  Rusanov flux at node {internal_interface1}: {F_rusanov[internal_interface1, internal_interface1-1:internal_interface1+2]}")
    print(f"  Rusanov flux at node {internal_interface2}: {F_rusanov[internal_interface2, internal_interface2-1:internal_interface2+2]}")
    
    # Verify Rusanov properties
    lambda_max = abs(wave_speed)
    
    # Check diffusion coefficients
    internal_interfaces = [ngl - 1, 2*ngl - 1]  # Right nodes of elements
    for i in internal_interfaces:
        rusanov_diffusion = F_rusanov[i, i] - 0.5 * wave_speed  # Subtract the average flux component
        print(f"\nDiffusion coefficient at node {i}: {rusanov_diffusion}, Expected: {0.5 * lambda_max}")
    
    # Visualize matrices
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(F_rusanov, cmap='RdBu', interpolation='nearest')
    plt.colorbar(label='Value')
    plt.title('Rusanov Flux Matrix')
    
    plt.subplot(1, 2, 2)
    plt.imshow(F_upwind, cmap='RdBu', interpolation='nearest')
    plt.colorbar(label='Value')
    plt.title('Upwind Flux Matrix')
    
    # Compare matrix structures
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.spy(F_rusanov, marker='o', markersize=8)
    plt.title('Rusanov Flux Matrix Structure')
    
    plt.subplot(1, 2, 2)
    plt.spy(F_upwind, marker='o', markersize=8)
    plt.title('Upwind Flux Matrix Structure')
    
    plt.tight_layout()
    plt.show()
    
    # Verification criteria
    print("\nVerification Summary:")
    
    # 1. Check that diagonal entries have the expected sign
    diag_entries_correct = all(F_rusanov[i, i] >= 0 for i in range(npoin))
    print(f"  Diagonal entries have correct sign: {diag_entries_correct}")
    
    # 2. Check that matrix is conservative (row sum is zero for interior nodes)
    row_sums = np.sum(F_rusanov, axis=1)
    interior_rows_conservative = all(abs(row_sums[1:-1]) < 1e-10)
    print(f"  Interior flux is conservative: {interior_rows_conservative}")
    
    # 3. Check that Rusanov adds more diffusion than upwind
    rusanov_abs_sum = np.sum(np.abs(F_rusanov))
    upwind_abs_sum = np.sum(np.abs(F_upwind))
    print(f"  Rusanov diffusion > Upwind diffusion: {rusanov_abs_sum > upwind_abs_sum}")
    print(f"  Rusanov sum: {rusanov_abs_sum}, Upwind sum: {upwind_abs_sum}")
    
    # 4. Check boundary handling
    left_bc_handled = abs(F_rusanov[0, 0] - (0.5 * wave_speed + 0.5 * lambda_max)) < 1e-10
    print(f"  Left boundary correctly handled: {left_bc_handled}")
    
    # Summary verdict
    if diag_entries_correct and interior_rows_conservative and rusanov_abs_sum > upwind_abs_sum and left_bc_handled:
        print("\n✅ Rusanov flux implementation looks correct!")
    else:
        print("\n❌ There may be issues with the Rusanov flux implementation.")

if __name__ == "__main__":
    test_rusanov_flux()