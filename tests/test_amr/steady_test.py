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
# xelem = np.array([-1, -0.6, -0.3,  0,  0.3, 0.6, 1])
xelem=np.array([-1, -0.5, -0.25, 0,0.5 ,1])
nelem = len(xelem) - 1
# 
# xelem = np.array([-1, -0.6, -0.3, -0.15, 0, 0.15, 0.3, 0.6, 1])
# nelem = len(xelem) - 1

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

Courant_max = 0.1           #dt controlled by courant_max
time_final = .1        #final time in revolutions
# iplot_solution = 1          #Switch to Plor of Not
# iplot_matrices = 0          #??????

icase = 1                #case number: 1 is a Gaussian, 2 is a square wave, 3 is a Gaussian with source, and 4 is a square wave with source
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
dt = Courant_max*dx/u
print(f'dt: {dt}')


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

Fmatrix_up = Fmatrix_upwind_flux_bc(intma, nelem, npoin, ngl, u)
Fmatrix_cent = Fmatrix_centered_flux(intma, nelem, npoin, ngl, u)

print(f'Fmat shape: {np.shape(Fmatrix_up)}')
# print(f'Fmatrix: {Fmatrix}')

bvec = np.zeros([npoin])
print(f'bvec shape: {np.shape(bvec)}')
bvec[0]=inflow_value
print(f'eff shape: {np.shape(f)}')

# Form right-hand side
rhs = Mmatrix @ f - Fmatrix_up @ bvec
print(f'Fmatrix_up @ bvec: {Fmatrix_up @ bvec}')
# rhs = Mmatrix @ f - Fmatrix_up @ bvec
print(f'rhs shape: {np.shape(rhs)}')

# Compute solution
epsilon = 1e-12
# A = Fmatrix_cent - Dmatrix + epsilon * np.eye(npoin_dg)
# q_numeric = np.linalg.solve(A, rhs)
q_numeric = np.linalg.solve(Fmatrix_up - Dmatrix, rhs)
# q_numeric = np.linalg.solve(Fmatrix_cent - Dmatrix, rhs)
print(f'q_numerical shape: {np.shape(q_numeric)}')
print(f'q_numeric: {q_numeric}')
print(f"F-D matrix condition number: {np.linalg.cond(Fmatrix_cent - Dmatrix)}")
residual = np.linalg.norm((Fmatrix_cent - Dmatrix) @ q_numeric - (Mmatrix @ f - Fmatrix_up @ bvec))
print(f"Solution residual: {residual}")



# ^^THIS IS NOT WORKING TAKE A CLOSER LOOK AT!!!!!


# Rmatrix = Dmatrix - Fmatrix

# print(f"Mass matrix condition number: {np.linalg.cond(Mmatrix)}")
# print(f"Sttiffness matrix condition number: {np.linalg.cond(Dmatrix)}")
# print(f"R matrix condition number: {np.linalg.cond(Rmatrix)}")


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([-1,1])
ymin = np.min(f)
ymax = np.max(f)
# ax.set_ylim([-0.2,1.6])
ax.set_ylim([ymin,ymax])
ax.set_xticks(xelem)
ax.tick_params(axis='x', rotation=90, labelsize=8)
ax.plot(coord, q_numeric, color = 'darkmagenta', ls ='--',label = 'numerical')
ax.plot(coord, qe, linewidth=10, alpha = 0.25, label = 'exact')
ax.plot(coord, f, color = 'darkcyan', label = 'forcing')
# ax.plot(coord, f, label = 'f')
ax.legend(loc='upper right')

print(f'stand alone coord shape: {(np.shape(coord))}')
print(f'stand alone coords: {coord}')
print(f'stand alone f: {f}')




#Create Grid

# # Adjust layout
# plt.tight_layout()
plt.show()

# print(f'\n\nForcing Function Integration:')
# for beta_val in [64, 128, 256]:
#     # Calculate forcing on fine grid
#     x_fine = np.linspace(-1, 1, 1000)
#     f_test = -2*u*beta_val*x_fine*np.exp(-beta_val*x_fine**2)
    
#     # Check total integral (should be near zero)
#     integral = np.trapz(f_test, x_fine)
#     print(f"Beta={beta_val}, Integral of forcing: {integral}")
    
#     # Check maximum value
#     print(f"Beta={beta_val}, Max forcing: {np.max(np.abs(f_test))}")


# print(f'\n\nBoundary Value Influence:')
# for beta_val in [64, 128, 256]:
#     # Calculate boundary value at x=-1
#     boundary_val = np.exp(-beta_val)
#     print(f"Beta={beta_val}, Boundary value at x=-1: {boundary_val}")
    
#     # Check influence in right-hand side
#     boundary_vec = np.zeros(npoin)
#     boundary_vec[0] = boundary_val
#     boundary_contrib = Fmatrix_up @ boundary_vec
#     print(f"Beta={beta_val}, Max boundary contribution: {np.max(np.abs(boundary_contrib))}")

# print(f'\n\nCondition Number Test:')
# for beta_val in [64, 128, 256]:
#     # Configure with this beta
#     # [...]
    
#     # Check condition numbers
#     cond_F = np.linalg.cond(Fmatrix_cent)
#     cond_D = np.linalg.cond(Dmatrix)
#     cond_system = np.linalg.cond(Fmatrix_cent - Dmatrix)
#     print(f"Beta={beta_val}, Condition numbers: F={cond_F}, D={cond_D}, F-D={cond_system}")





# # q0 = qe
# # X = np.linalg.solve(Rmatrix, Mmatrix)
# # # Multiply X by fe
# # result = X @ f  # or np.dot(X, fe)

# # # Negate the result
# # qc = -result
# # qc = np.zeros(len(coord))

# # qc = -1*np.linalg.solve(Rmatrix, Mmatrix @ f)
# Dhat = np.linalg.solve(Mmatrix,Rmatrix)

# qc, time, plots, exact, grids, xelems = ti_LSRK_steady(qe, f, Dhat, periodicity, xgl, xelem, wnq, xnq, psi, dpsi,u, time, time_final, dt, 
#                 icase, max_level, criterion)


# print(qc)

# ax.plot(coord,qe, linestyle=':',label = 'exact solution')
# ax.plot(coord, qc, label = 'computed solution')
# ax.legend(loc='upper right')

# # # Adjust layout
# plt.tight_layout()
# plt.show()
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

