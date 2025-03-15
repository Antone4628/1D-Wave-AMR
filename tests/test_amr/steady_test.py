import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from matplotlib.animation import FuncAnimation
import os
import sys
import os.path
import traceback

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

ANIMATIONS_DIR = os.path.join(PROJECT_ROOT, 'animations')
os.makedirs(ANIMATIONS_DIR, exist_ok=True)

from numerical.dg.basis import lgl_gen, Lagrange_basis
from numerical.dg.matrices import *
from numerical.grid.mesh import create_grid_us
from numerical.amr.forest import forest
from numerical.solvers.utils import exact_solution, eff
from numerical.solvers.wave import *

# from numerical.amr.adapt import adapt_mesh
# from numerical.amr.projection import create_S_matrix, create_scatters, create_gathers


# xelem=np.array([-1,  0 ,0.3 ,1])
# nelem = 3                 #Initial number of elements in level zero

# xelem=np.array([-1, -0.3 ,0 ,0.3 ,1])
# xelem=np.array([-1, -0.4, 0 ,0.4 ,1])
# nelem = 4                 #Initial number of elements in level zero
# xelem=np.array([-1, -0.5, 0 ,0.5 ,1])
# nelem = 4                 #Initial number of elements in level zero

xelem = np.array([-1, -0.6, -0.3, -0.15, 0, 0.15, 0.3, 0.6, 1])
nelem = len(xelem) - 1

# xelem=np.array([-1, -0.6 ,-0.2, 0.2 ,0.6 ,1])
# nelem = 5                 #Initial number of elements in level zero

# xelem=np.array([-1, -0.9, -0.8, -0.7, -0.6, -0.5,  -0.4, -0.3, -0.2, -0.1
#                  ,0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ,1])
# nelem = 20                 #Initial number of elements in level zero

# xelem=np.array([-1, -0.95, -0.9, -0.85, -0.8, -0.75, -0.7,-0.65, -0.6,-0.55, -0.5,
#                 -0.45,  -0.4, -0.35, -0.3, -0.25,-0.2, -0.15,-0.1,
#                 -0.05, 0,0.05, 0.1,0.15, 0.2,0.25, 0.3,0.35, 0.4,0.45, 0.5,0.55,
#                   0.6,0.65, 0.7,0.75, 0.8,0.85, 0.9 ,0.95,1])
# nelem = 40                 #Initial number of elements in level zero

differences = np.diff(xelem)
print(f'element sizes: {differences}')

# Find the minimum difference
min_interval = np.min(differences)
print(f'smallest element has dx: {min_interval}')

max_level = 4         #Max level of refinement
criterion = 1        #AMR Criterion type
cur_level = 0
nop = 4
ngl = nop + 1

dx_min = min_interval/(2**max_level)
print(f'smallest refined element: {dx_min}')
# dt_opt = Courant_max*dx_min/u

npoin_cg = nop*nelem + 1
npoin_dg = ngl*nelem



integration_points = 1      #=1 for LGL and =2 for LG
integration_type = 2        #=1 is inexact and =2 is exact
space_method_type = 'dg'    #CG or DG
# flux_type = 2               #1=centered flux and 2=upwind

# Courant_max = 0.1           #dt controlled by courant_max
# time_final = .2        #final time in revolutions
# iplot_solution = 1          #Switch to Plor of Not
# iplot_matrices = 0          #??????

icase = 8                #case number: 1 is a Gaussian, 2 is a square wave, 3 is a Gaussian with source, and 4 is a square wave with source
xmu = 0.05                  #filtering strength: 1 is full strength and 0 is no filter
ifilter = 0                 #time-step frequency that the filter is applied. 0=never, 1 = every time-step



#Compute Interpolation and Integration Points
xgl,wgl = lgl_gen(ngl)
if (integration_points ==1):
    integration_text = 'LGL'
    if (integration_type ==1):
        noq = nop
    elif (integration_type ==2):
        noq = nop + 1
    nq = noq + 1
    xnq,wnq = lgl_gen(nq)


psi, dpsi = Lagrange_basis(ngl,nq, xgl, xnq)
row_sum_psi = sum(psi)
row_sum_dpsi = sum(dpsi)

#Create Grid
coord_dg,  intma_dg, periodicity_dg  = create_grid_us(ngl,nelem,npoin_cg,npoin_dg,xgl, xelem)

#Form Global Matrix and Periodic BC Pointers
if (space_method_type == 'dg'):
    npoin = npoin_dg
    coord = coord_dg
    intma = intma_dg
    periodicity = periodicity_dg
    print(f'{space_method_type} : {integration_text}')

#Compute Exact Solution:
time = 0
qe, u = exact_solution(coord, npoin, time, icase)
fcase = icase
f = eff(coord, npoin, fcase, u)
# Define inflow boundary condition (at x = -1 if wave speed > 0)
inflow_value = exact_solution(np.array([-1]), 1, time, icase)[0]  # Exact solution at inflow


#Compute Courant Number
dx = coord[1]-coord[0]


#Get AMR data structures
label_mat, info_mat, active_grid = forest(xelem, max_level)


#Create Local/Element Mass and Differentiation Matrices
Me = create_mass_matrix(intma, coord, nelem, ngl, nq, wnq, psi)
De = create_diff_matrix(ngl, nq, wnq, psi, dpsi)

#Form Global Matrices

# modify the periodicity array for non-periodic:
periodicity_non_periodic = np.arange(npoin_dg)  # Identity mapping (no periodicity)

# When assembling matrices
Mmatrix, Dmatrix = Matrix_DSS(Me, De, u, intma, periodicity_non_periodic, ngl, nelem, npoin)

# Fmatrix = Fmatrix_upwind_flux(intma, nelem, npoin, ngl, u)
# ^^THIS IS NOT WORKING TAKE A CLOSER LOOK AT!!!!!

def create_manual_upwind_flux(intma, nelem, npoin, ngl, u):
    """
    Creates a manual upwind flux matrix for steady-state advection with debugging.
    """
    F = np.zeros((npoin, npoin))
    
    # Print debug information to track interface connections
    print("Element interface connectivity:")
    
    for e in range(nelem):
        # Left edge of current element
        i_left = 0
        I_left = intma[i_left][e]
        
        # Right edge of current element
        i_right = ngl - 1
        I_right = intma[i_right][e]
        
        # Internal interfaces - left edge connects to previous element
        if e > 0:  # Not the first element
            I_prev = intma[ngl-1][e-1]  # Right edge of previous element
            print(f"Interface between elements {e-1} and {e}: points {I_prev} ⟷ {I_left}")
            
            if u > 0:  # Flow from left to right
                # Flux at interface (left edge receives flux from previous element)
                F[I_left][I_prev] = u  # Take value from upwind (prev element)
                F[I_left][I_left] = -u  # Subtract own value
            else:  # Flow from right to left
                # For negative velocity, upwind is now the current element
                F[I_left][I_left] = -u  # Take value from current element (upwind)
                F[I_left][I_prev] = u  # Subtract prev element value
        
        # Internal interfaces - right edge connects to next element
        if e < nelem - 1:  # Not the last element
            I_next = intma[0][e+1]  # Left edge of next element
            print(f"Interface between elements {e} and {e+1}: points {I_right} ⟷ {I_next}")
            
            if u > 0:  # Flow from left to right
                # For positive velocity, upwind is the current element
                F[I_right][I_right] = u  # Take value from current element (upwind)
                F[I_right][I_next] = -u  # Subtract next element value
            else:  # Flow from right to left
                # Flux at interface (right edge receives flux from next element)
                F[I_right][I_next] = -u  # Take value from upwind (next element)
                F[I_right][I_right] = u  # Subtract own value
    
    # Handle domain boundaries
    # Left boundary (x = -1)
    if u > 0:  # Inflow from left
        I_left_boundary = intma[0][0]
        print(f"Left boundary (inflow): point {I_left_boundary}")
        # Zero the row but set diagonal to 1 (Dirichlet-type)
        F[I_left_boundary, :] = 0
        F[I_left_boundary, I_left_boundary] = 1  # Identity for Dirichlet
    else:  # Outflow to left
        I_left_boundary = intma[0][0]
        print(f"Left boundary (outflow): point {I_left_boundary}")
        F[I_left_boundary][I_left_boundary] = -u  # Standard outflow treatment
    
    # Right boundary (x = 1)
    if u > 0:  # Outflow to right
        I_right_boundary = intma[ngl-1][nelem-1]
        print(f"Right boundary (outflow): point {I_right_boundary}")
        F[I_right_boundary][I_right_boundary] = u  # Standard outflow treatment
    else:  # Inflow from right
        I_right_boundary = intma[ngl-1][nelem-1]
        print(f"Right boundary (inflow): point {I_right_boundary}")
        F[I_right_boundary, :] = 0
        F[I_right_boundary, I_right_boundary] = 1  # Identity for Dirichlet
    
    # Print non-zero entries for verification
    print("\nNon-zero flux matrix entries:")
    non_zeros = np.where(F != 0)
    for i, j in zip(non_zeros[0], non_zeros[1]):
        print(f"F[{i},{j}] = {F[i,j]}")
    
    return F

Fmatrix =create_manual_upwind_flux(intma, nelem, npoin, ngl, u)

rhs = Mmatrix @ f
# if u > 0:  # Inflow from left
#     I_left_boundary = intma[0][0]
#     rhs[I_left_boundary] += u * inflow_value
# else:  # Inflow from right
#     I_right_boundary = intma[ngl-1][nelem-1]
#     rhs[I_right_boundary] -= u * inflow_value


# system matrix sign ??????
system_matrix = -Dmatrix + Fmatrix 

if u > 0:  # Inflow from left
    I_left_boundary = intma[0][0]
    # Zero the row in system matrix 
    # System_matrix[I_left_boundary, :] = 0
    
    # Set diagonal to 1 for Dirichlet condition
    system_matrix[I_left_boundary, I_left_boundary] = 1
    
    # Set right-hand side to boundary value
    rhs[I_left_boundary] = inflow_value
 
# # Solve the system
qc = np.linalg.solve(system_matrix, rhs)


# print(f"Wave speed: {u}")
# print(f"Inflow value: {inflow_value}")
# print(f"First few rows of Dmatrix:\n{Dmatrix[:5,:5]}")
# print(f"First few rows of Fmatrix:\n{Fmatrix[:5,:5]}")
# print(f"First few values of RHS vector:\n{rhs[:5]}")
# print(f"First few values of computed solution:\n{qc[:5]}")
# print(f"First few entries of system matrix:\n{system_matrix[:5,:5]}")

# check for any zero rows in the system matrix
# zero_rows = np.where(np.all(system_matrix == 0, axis=1))[0]
# if len(zero_rows) > 0:
#     print(f"System matrix has zero rows at indices: {zero_rows}")

# print(f"Element connectivity matrix (intma):\n{intma}")
# print(f'coord array: {coord}')
print(f"Exact solution at left boundary (x=-1): {exact_solution(np.array([-1.0]), 1, time, icase)[0]}")
print(f"Exact solution at right boundary (x=1): {exact_solution(np.array([1.0]), 1, time, icase)[0]}")
# cond_num = np.linalg.cond(system_matrix)
# print(f"Condition number of system matrix: {cond_num}")

# Check the structure of the matrices
# print(f"Mass matrix shape: {Mmatrix.shape}")
# print(f"F matrix shape: {F.shape}")
# print(f"D matrix shape: {Dmatrix.shape}")
# print(f"System matrix shape: {system_matrix.shape}")

# print(f"Mass matrix: {Mmatrix}")
# print(f"F matrix: {F}")
# print(f"D matrix: {Dmatrix}")
# print(f"System matrix: {system_matrix}")

# qc = np.linalg.solve(system_matrix, rhs)
# system_matrix = -u*Dmatrix + F

# R = np.linalg.solve(system_matrix, Mmatrix)

# # #Apply BCs
# # if(flux_type == 2):
# #     Fmatrix = Fmatrix_upwind_flux(intma, nelem, npoin, ngl, u)
# # Rinv = np.linalg.inv(R)
# # Rmatrix = np.matmul(Rinv,Mmatrix)
# # Rmatrix = np.matmul(Mmatrix,Rinv)



# qc = R @ f
# # qc = np.matmul(Rmatrix,f)
# print(qc)





# #Left-Multiply by Inverse Mass Matrix
# # Dmatrix_hat=Mmatrix\Rmatrix
# Dmatrix_hat = np.linalg.solve(Mmatrix,Rmatrix)




# Check condition number of element matrices
for e in range(nelem):
    local_mass = np.zeros((ngl, ngl))
    for i in range(ngl):
        for j in range(ngl):
            local_mass[i,j] = Me[e,i,j]
    print(f"Element {e} mass matrix condition number: {np.linalg.cond(local_mass)}")

# Check flux conservation at interfaces
for e in range(1, nelem):
    I_right = intma[ngl-1][e-1]  # Right edge of previous element
    I_left = intma[0][e]        # Left edge of current element
    flux_right = Fmatrix[I_right,:]  # Outflow from element e-1
    flux_left = Fmatrix[I_left,:]    # Inflow to element e
    flux_diff = np.sum(flux_right) + np.sum(flux_left)
    print(f"Interface {e}: Flux imbalance: {flux_diff}")


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([-1,1])
ax.set_ylim([-1.1,6.5])
ax.set_xticks(xelem)
ax.tick_params(axis='x', rotation=90, labelsize=8)
ax.plot(coord, f, label = 'f')
ax.plot(coord,qe, label = 'exact solution')
ax.plot(coord, qc, label = 'computed solution')
ax.legend(loc='upper right')

# Adjust layout
plt.tight_layout()
plt.show()
# ax.set_title(f'{nelem} initial elements, full AMR to level {max_level}, dt = {dt:.6f}')
# frame_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)
# time_text = ax.text(0.05, 0.90,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)


# animated_plot = ax.plot(grids[0][:],solutions[0][:], color = 'darkmagenta')[0]

# def update_data(frame):
#     animated_plot.set_ydata(solutions[frame][:])
#     animated_plot.set_xdata(grids[frame][:])
#     ax.set_xticks(xelems[frame][:])
#     frame_text.set_text('frame: %.1d' % frame)
#     time = frame*dt
#     time_text.set_text('time: %.2f' % time)

# #     return animated_plot

# anim = FuncAnimation(fig = fig,
#                           func = update_data,
#                           frames = len(solutions),
#                           interval = 10)

# gif_title = '1D_Wave_AMR_refdef'+'_GIF.gif'
# # Save as gif file
# # anim.save(gif_title, writer = "pillow", fps=50 )
# gif_title = os.path.join(ANIMATIONS_DIR, '1D_Wave_AMR_refdef_GIF.gif')
# anim.save(gif_title, writer="pillow", fps=50)
# # plt.show()
# # plt.close()
# # HTML(anim.to_html5_video())
# # content/drive/MyDrive/ColabNotebooks/Galerkin/

# # plt.draw()
# # plt.show()
# # plt.draw()
# anim

