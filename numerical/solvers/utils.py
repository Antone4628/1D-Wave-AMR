import numpy as np

def exact_solution(coord, npoin, time, icase):
    """
    Computes exact solution for test cases.
    
    Args:
        coord (array): Grid coordinates
        npoin (int): Number of points
        time (float): Current time
        icase (int): Test case number (1-9)
        
    Returns:
        tuple: (qe, u) Solution values and wave speed
    """
    # constants
    w = 1
    visc = 0
    h = 0
    xc = 0
    xmin = -1
    xmax = 1
    x1 = xmax-xmin
    sigma0 = 0.125
    rc = 0.125
    sigma = np.sqrt(sigma0**2 + 2*visc*time)
    u = w*x1
    alph = 1.0
    # beta = 64.0
    # beta = 128.0
    beta = 256.0
    # beta = 512.0
    
    # initialize
    qe = np.zeros(npoin)
    
    timec = time - np.floor(time)
    
    for i in range(npoin):
        x = coord[i]
        xbar = xc + u*timec
        if(xbar > xmax):
            xbar = xmin + (xbar-xmax)
        r = x-xbar
        domain_length = xmax - xmin
        r = r - domain_length * np.round(r / domain_length)
        
        if(icase == 1):
            qe[i] = np.exp(-beta*(x-xbar)**2)
        elif(icase == 2):
            if(abs(r) <= rc):
                qe[i] = 1
        elif(icase == 3):
            qe[i] = sigma0/sigma*np.exp(-(x-xbar)**2/(2*sigma**2))
        elif(icase == 4):
            if(abs(r) <= rc):
                qe[i] = 1
        elif(icase == 5):
            if(x <= xc):
                qe[i] = 1
        elif(icase == 6):
            qe[i] = np.sin(((x + 1)*np.pi)/2.0)
        elif(icase ==7):
            qe[i] = 1-np.tanh(alph*(1-4*((x)-1/4)))
        elif(icase == 8):
            qe[i]= np.sin(np.pi * x)

        elif(icase == 9):
            # Section 4.3 unsteady Gaussian pulse from the paper
            # Parameters: mu = -4, sigma^2 = 0.25, c = 1
            mu = -4
            sigma_sq = 0.25
            c = 1.0
            
            # The solution for the advection equation with constant velocity c
            # is u(x,t) = u0(x - ct)
            x_shifted = x - c*time
            
            # CRITICAL FIX: To properly handle periodic boundaries, we need to consider
            # contributions from all periodic images of the Gaussian
            domain_length = 8
            
            # Sum contributions from the main pulse and one periodic image on each side
            # This ensures smoothness at the boundaries
            main_pulse = np.exp(-1/(2*sigma_sq)*((x_shifted - mu)**2))
            left_image = np.exp(-1/(2*sigma_sq)*((x_shifted - mu + domain_length)**2))
            right_image = np.exp(-1/(2*sigma_sq)*((x_shifted - mu - domain_length)**2))
            
            # The final solution is the sum of all contributions
            qe[i] = main_pulse + left_image + right_image
            
            # Use unit wave speed for this case
            u = 1.0
        # elif(icase == 9):
        #     # Section 4.3 unsteady Gaussian pulse from the paper
        #     # Parameters: mu = -4, sigma^2 = 0.25, c = 1
        #     mu = -4
        #     sigma_sq = 0.25
        #     c = 1
            
        #     # The solution for the advection equation with constant velocity c
        #     # is u(x,t) = u0(x - ct)
        #     x_shifted = x - c*time
            
        #     # Apply periodic boundary if needed (domain is [-4,4])
        #     domain_length = 8
        #     if x_shifted < -4:
        #         x_shifted += domain_length
        #     elif x_shifted > 4:
        #         x_shifted -= domain_length
                
        #     # Gaussian pulse: exp(-1/(2*sigma^2)*(x-mu)^2)
        #     qe[i] = np.exp(-1/(2*sigma_sq)*(x_shifted - mu)**2)
            
        #     # Use unit wave speed for this case
        #     u = 1.0
    
    return qe, u

# def eff(coord, npoin, fcase, u):
#     """
#     Computes exact solution for test cases.
    
#     Args:
#         coord (array): Grid coordinates
#         npoin (int): Number of points
#         time (float): Current time
#         icase (int): Test case number (1-6)
        
#     Returns:
#         tuple: (qe, u) Solution values and wave speed
#     """
#     # constants
#     w = 1
#     xc = 0
#     xmin = -1
#     xmax = 1
#     x1 = xmax-xmin
#     sigma0 = 0.125
#     rc = 0.125
#     u = w*x1
#     alph = 1.0
#     # beta = 64.0
#     # beta = 128.0
#     beta = 256.0
#     # beta = 512.0
    
#     # initialize
#     f = np.zeros(npoin)
#     # print("Initial qe:", qe)  # Debug print
    
#     # timec = time - np.floor(time)

    
#     for i in range(npoin):
#         x = coord[i]
        

#         if(fcase == 1):
#             f[i] = -2*u*beta*x*np.exp(-beta*x**2)
#         elif(fcase == 7):

#             def sech(x):
#                 return 1 / np.cosh(x)

#             inner = alph * (1 - 4 * (x - 1/4))
    
#             # f[i] = (4*alph)/((np.cosh(alph*(1-4*(x-1/4))))**2)
#             f[i] = 4 * alph * sech(inner)**2
#         elif(fcase == 8 ):
#             f[i] =  u*np.pi * np.cos(np.pi * x)
#         elif(fcase == 9):
#             # Force for Gaussian pulse (should be zero for pure advection)
#             f[i] = 0

#     return f

def eff(coord, npoin, fcase, wave_speed, time=0.0):
    """
    Computes forcing function with proper time-dependency to match exact solution.
    
    Args:
        coord (array): Grid coordinates
        npoin (int): Number of points
        fcase (int): Test case number
        wave_speed (float): Wave speed
        time (float): Current simulation time
        
    Returns:
        array: Forcing function values
    """
    # Constants (matching those in exact_solution)
    w = 1
    xc = 0
    xmin = -1
    xmax = 1
    x1 = xmax-xmin
    sigma0 = 0.125
    rc = 0.125
    alph = 1.0
    beta = 256.0
    
    # Initialize forcing vector
    f = np.zeros(npoin)
    
    # Time computation (same as in exact_solution)
    timec = time - np.floor(time)
    
    for i in range(npoin):
        x = coord[i]
        
        # Calculate the center position (moves with time)
        xbar = xc + wave_speed*timec
        if xbar > xmax:
            xbar = xmin + (xbar-xmax)
        
        if fcase == 1:
            # Correct forcing for moving Gaussian: u * d/dx[exp(-beta*(x-xbar)^2)]
            f[i] = -2*wave_speed*beta*(x-xbar)*np.exp(-beta*(x-xbar)**2)
        
        elif fcase == 7:
            # Forcing for tanh solution
            def sech(x):
                return 1 / np.cosh(x)
            inner = alph * (1 - 4 * (x - 1/4))
            f[i] = 4 * alph * sech(inner)**2
        
        elif fcase == 8:
            # Forcing for sine solution
            f[i] = wave_speed*np.pi * np.cos(np.pi * x)
        
        elif fcase == 9:
            # Forcing for Gaussian pulse (should be zero for pure advection)
            f[i] = 0
    
    return f

def L2_err_norm(nop, nelem, q0, qe):
    """
    Computes L2 error norm between numerical and exact solutions.
    
    Args:
        nop (int): Polynomial order
        nelem (int): Number of elements
        q0 (array): Numerical solution
        qe (array): Exact solution
        
    Returns:
        float: L2 error norm
    """
    Np = nelem*nop + 1
    num = 0
    den = 0
    for i in range(Np):
        num = num + (qe[i]-q0[i])**2
        den = den + qe[i]**2
    err = np.sqrt(num/den)

    return err

def L2normerr(q0, qe):
    num = np.norm(q0, qe)
    den = np.norm(qe)
    err = num/den
    return err

def calculate_grid_normalized_l2_error(final_solution, final_coord, initial_coord, time_final, icase):
    """
    Calculate L2 error by projecting final solution back to initial grid for fair comparison.
    
    This function interpolates the final numerical solution (computed on an adapted mesh)
    back onto the initial uniform grid, then computes the L2 error relative to the exact
    solution on that same initial grid. This provides mesh-independent error comparison.
    
    Args:
        final_solution (array): Numerical solution on final adapted mesh
        final_coord (array): Coordinate points of final adapted mesh  
        initial_coord (array): Coordinate points of initial uniform mesh
        time_final (float): Final simulation time
        icase (int): Test case identifier
    
    Returns:
        float: Grid-normalized L2 error (mesh-independent)
    """
    # Interpolate final solution onto initial grid coordinates
    solution_on_initial_grid = np.interp(initial_coord, final_coord, final_solution)
    
    # Calculate exact solution on initial grid
    exact_on_initial_grid, _ = exact_solution(initial_coord, len(initial_coord), time_final, icase)
    
    # Calculate L2 norm on consistent grid
    grid_normalized_l2_error = np.sqrt(
        np.sum((solution_on_initial_grid - exact_on_initial_grid)**2) / 
        np.sum(exact_on_initial_grid**2)
    )
    
    return grid_normalized_l2_error


def compute_total_mass(q, Me, intma):
    """
    Compute total mass (integral of solution) using mass matrix
    """
    print(f'intma:\n {intma[0][:]}')
    mass = 0
    for e in range(len(intma[0][:])):  # loop over elements
        # Get local solution and mass matrix
        print(f'intma[e]: {intma[:,e]}')
        q_local = q[intma[:,e]]
        Me_local = Me[e]
        # Add contribution from this element
        mass += np.dot(np.dot(q_local, Me_local), q_local)
    return mass


# import numpy as np

# def exact_solution(coord, npoin, time, icase):
#     """
#     Computes exact solution for test cases.
    
#     Args:
#         coord (array): Grid coordinates
#         npoin (int): Number of points
#         time (float): Current time
#         icase (int): Test case number (1-6)
        
#     Returns:
#         tuple: (qe, u) Solution values and wave speed
#     """
#     # constants
#     w = 1
#     visc = 0
#     h = 0
#     xc = 0
#     xmin = -1
#     xmax = 1
#     x1 = xmax-xmin
#     sigma0 = 0.125
#     rc = 0.125
#     sigma = np.sqrt(sigma0**2 + 2*visc*time)
#     u = w*x1
#     alph = 1.0
#     # beta = 64.0
#     beta = 256.0
    
#     # initialize
#     qe = np.zeros(npoin)
#     # print("Initial qe:", qe)  # Debug print
    
#     timec = time - np.floor(time)
    
#     for i in range(npoin):
#         x = coord[i]
#         xbar = xc + u*timec
#         if(xbar > xmax):
#             xbar = xmin + (xbar-xmax)
#         r = x-xbar
        
#         if(icase == 1):
#             qe[i] = np.exp(-beta*(x-xbar)**2)
#         elif(icase == 2):
#             if(abs(r) <= rc):
#                 qe[i] = 1
#         elif(icase == 3):
#             qe[i] = sigma0/sigma*np.exp(-(x-xbar)**2/(2*sigma**2))
#         elif(icase == 4):
#             if(abs(r) <= rc):
#                 qe[i] = 1
#         elif(icase == 5):
#             if(x <= xc):
#                 qe[i] = 1
#         elif(icase == 6):
#             qe[i] = np.sin(((x + 1)*np.pi)/2.0)

#         elif(icase ==7):
#             qe[i] = 1-np.tanh(alph*(1-4*((x)-1/4)))

#         elif(icase == 8):
#             qe[i]= np.sin(np.pi * x)
#             # print(f"Just assigned qe[{i}] = {qe[i]}")  # Debug print
        
#         # print(f"After iteration {i}, qe = {qe}")  # Debug print
    
#     # print("Final qe before return:", qe)  # Debug print
#     return qe, u

# def eff(coord, npoin, fcase, u):
#     """
#     Computes exact solution for test cases.
    
#     Args:
#         coord (array): Grid coordinates
#         npoin (int): Number of points
#         time (float): Current time
#         icase (int): Test case number (1-6)
        
#     Returns:
#         tuple: (qe, u) Solution values and wave speed
#     """
#     # constants
#     w = 1
#     xc = 0
#     xmin = -1
#     xmax = 1
#     x1 = xmax-xmin
#     sigma0 = 0.125
#     rc = 0.125
#     u = w*x1
#     alph = 1.0
#     # beta = 64.0
#     beta = 256.0
    
#     # initialize
#     f = np.zeros(npoin)
#     # print("Initial qe:", qe)  # Debug print
    
#     # timec = time - np.floor(time)

    
#     for i in range(npoin):
#         x = coord[i]
        
#         if(fcase == 7):

#             def sech(x):
#                 return 1 / np.cosh(x)

#             inner = alph * (1 - 4 * (x - 1/4))
    
#             # f[i] = (4*alph)/((np.cosh(alph*(1-4*(x-1/4))))**2)
#             f[i] = 4 * alph * sech(inner)**2
#         elif(fcase == 8 ):
#             f[i] =  u*np.pi * np.cos(np.pi * x)

#     return f

# def L2_err_norm(nop, nelem, q0, qe):
#     """
#     Computes L2 error norm between numerical and exact solutions.
    
#     Args:
#         nop (int): Polynomial order
#         nelem (int): Number of elements
#         q0 (array): Numerical solution
#         qe (array): Exact solution
        
#     Returns:
#         float: L2 error norm
#     """
#     Np = nelem*nop + 1
#     num = 0
#     den = 0
#     for i in range(Np):
#         num = num + (qe[i]-q0[i])**2
#         den = den + qe[i]**2
#     err = np.sqrt(num/den)

#     return err

# def L2normerr(q0, qe):
#     num = np.norm(q0, qe)
#     den = np.norm(qe)
#     err = num/den
#     return err


# def compute_total_mass(q, Me, intma):
#     """
#     Compute total mass (integral of solution) using mass matrix
#     """
#     print(f'intma:\n {intma[0][:]}')
#     mass = 0
#     for e in range(len(intma[0][:])):  # loop over elements
#         # Get local solution and mass matrix
#         print(f'intma[e]: {intma[:,e]}')
#         q_local = q[intma[:,e]]
#         Me_local = Me[e]
#         # Add contribution from this element
#         mass += np.dot(np.dot(q_local, Me_local), q_local)
#     return mass