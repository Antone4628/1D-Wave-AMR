# Compare values to MATLAB values:

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
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

def matrix_to_string(M, precision=6):
    """Convert a matrix to a formatted string representation, handling 1D, 2D, and 3D arrays"""
    # Handle 1D arrays
    if M.ndim == 1:
        M = M.reshape(1, -1)
        
    # Handle 3D arrays - flatten to 2D by concatenating along rows
    if M.ndim == 3:
        rows_total = M.shape[0] * M.shape[1]
        cols = M.shape[2]
        M_2d = np.zeros((rows_total, cols))
        
        row_idx = 0
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                M_2d[row_idx] = M[i, j]
                row_idx += 1
        
        M = M_2d
    
    # Now M should be 2D
    rows, cols = M.shape
    result = "["
    
    for i in range(rows):
        if i > 0:
            result += "\n "  # New line for each row after the first
        
        for j in range(cols):
            if isinstance(M[i, j], (int, np.integer)):
                value = f"{int(M[i, j])}"
            else:
                value = f"{M[i, j]:.{precision}g}"
                
            result += value
            if j < cols - 1:
                result += ", "
        
        if i < rows - 1:
            result += ";"
    
    result += "]"
    return result

def save_matrices_to_pdf(nop, nelem, ngl, nq, npoin_cg, npoin_dg, u, xgl, wgl, xnq, wnq,
                        psi, dpsi, De, coord_cg, coord_dg, intma_cg, intma_dg,
                        periodicity_cg, periodicity_dg, Me, Fmatrix, M, D, Rmatrix):
    
    # Create a PDF
    with PdfPages('python_matrices_comparison.pdf') as pdf:
        # Create a figure with a specific size (A4 paper)
        fig = plt.figure(figsize=(8.27, 11.69))
        gs = gridspec.GridSpec(1, 1)
        ax = plt.subplot(gs[0])
        ax.axis('off')
        
        # String to hold all the text
        report_text = "Scalar Parameters:\n"
        report_text += f"nop = {nop}\n"
        report_text += f"nelem = {nelem}\n"
        report_text += f"ngl = {ngl}\n"
        report_text += f"nq = {nq}\n"
        report_text += f"npoin_cg = {npoin_cg}\n"
        report_text += f"npoin_dg = {npoin_dg}\n"
        report_text += f"u = {u}\n\n"
        
        # Add vectors
        report_text += "Legendre Gauss Lobatto Points (xgl):\n"
        report_text += matrix_to_string(xgl.reshape(1, -1), 6) + "\n\n"
        
        report_text += "Legendre Gauss Lobatto Weights (wgl):\n"
        report_text += matrix_to_string(wgl.reshape(1, -1), 6) + "\n\n"
        
        report_text += "Quadrature Points (xnq):\n"
        report_text += matrix_to_string(xnq.reshape(1, -1), 6) + "\n\n"
        
        report_text += "Quadrature Weights (wnq):\n"
        report_text += matrix_to_string(wnq.reshape(1, -1), 6) + "\n\n"
        
        # Add matrices
        report_text += "Differentiation Matrix (De):\n"
        report_text += matrix_to_string(De, 6) + "\n\n"
        
        report_text += "CG Coordinates (coord_cg):\n"
        report_text += matrix_to_string(coord_cg.reshape(1, -1), 6) + "\n\n"
        
        report_text += "DG Coordinates (coord_dg):\n"
        report_text += matrix_to_string(coord_dg.reshape(1, -1), 6) + "\n\n"
        
        report_text += "CG Connectivity (intma_cg):\n"
        report_text += matrix_to_string(intma_cg, 0) + "\n\n"
        
        report_text += "DG Connectivity (intma_dg):\n"
        report_text += matrix_to_string(intma_dg, 0) + "\n\n"
        
        report_text += "CG Periodicity (periodicity_cg):\n"
        report_text += matrix_to_string(periodicity_cg.reshape(1, -1), 0) + "\n\n"
        
        report_text += "DG Periodicity (periodicity_dg):\n"
        report_text += matrix_to_string(periodicity_dg.reshape(1, -1), 0) + "\n\n"
        
        # Add Lagrange bases
        report_text += "Lagrange Basis (psi):\n"
        report_text += matrix_to_string(psi, 6) + "\n\n"
        
        report_text += "Lagrange Basis Derivative (dpsi):\n"
        report_text += matrix_to_string(dpsi, 6) + "\n\n"
        
        # Add larger matrices - might need multiple pages
        report_text += "Mass Matrix (Me):\n"
        report_text += matrix_to_string(Me, 6) + "\n\n"
        
        # Place the text on the figure
        ax.text(0.05, 0.95, report_text, va='top', fontsize=8, family='monospace')
        pdf.savefig(fig)
        plt.close(fig)
        
        # Create a new page for the remaining matrices
        fig = plt.figure(figsize=(8.27, 11.69))
        gs = gridspec.GridSpec(1, 1)
        ax = plt.subplot(gs[0])
        ax.axis('off')
        
        report_text = "Upwind Flux Matrix (Fmatrix):\n"
        report_text += matrix_to_string(Fmatrix, 6) + "\n\n"
        
        report_text += "Global Mass Matrix (M):\n"
        report_text += matrix_to_string(M, 6) + "\n\n"
        
        report_text += "Global Differentiation Matrix (D):\n"
        report_text += matrix_to_string(D, 6) + "\n\n"
        
        report_text += "Rmatrix (D-Fmatrix):\n"
        report_text += matrix_to_string(Rmatrix, 6) + "\n\n"
        
        # Place the text on the figure
        ax.text(0.05, 0.95, report_text, va='top', fontsize=8, family='monospace')
        pdf.savefig(fig)
        plt.close(fig)
    
    print(f"All matrices and values saved to python_matrices_comparison.pdf")



# xelem=np.array([-1,  0 ,0.3 ,1])
# nelem = 3                 #Initial number of elements in level zero

# xelem=np.array([-1, -0.3 ,0 ,0.3 ,1])
# xelem=np.array([-1, -0.4, 0 ,0.4 ,1])
# nelem = 4                 #Initial number of elements in level zero
xelem=np.array([-1, -0.5, 0 ,0.5 ,1])
nelem = 4                 #Initial number of elements in level zero

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
    nq = 6
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

Fmatrix = Fmatrix_upwind_flux(intma, nelem, npoin, ngl, u)
# ^^THIS IS NOT WORKING TAKE A CLOSER LOOK AT!!!!!

Rmatrix = Dmatrix - Fmatrix

save_matrices_to_pdf(
    nop, nelem, ngl, nq, npoin_cg, npoin_dg, u, xgl, wgl, xnq, wnq, 
    psi, dpsi, De, coord, coord_dg, np.array([[0]]), intma_dg, 
    np.array([0]), periodicity_dg, Me, Fmatrix, Mmatrix, Dmatrix, Rmatrix
)

