"""
Module that allows to generate and display a Brownian trajectory.

Calculations are performed using the Langevin equation, considering a
Gaussian-type random force.

Time is discretized, and the particle's position is in a single dimension x.
"""

### Import of modules
import matplotlib.pyplot as plt
import random
plt.ion() # Interactive mode activated
plt.style.use('bmh')

### Definition of functions
# Main functions of the algorithm
def move_particle(xi, v, dt):
    """
    Updates the position of the particle according to a Brownian trajectory.

    Parameters
    ----------
    xi : float, optional
        Particle position at time ti
    V : float
        Speed
    dt : float
        Elementary time step

    Returns
    -------
    xip1 : float
        Brownian particle position at time i+1
    """
    eps = random.choice([-1, 1])
    xip1 = xi + eps*v*dt
    return xip1

def move_particle2D(xi, yi, v, dt, prob):
    """
    Parameters
    ----------
    xi : float
        Particle position in the X-axis.
    yi : float
        Particle position in the Y-axis.
    v : TYPE
        Speed.
    dt : float
        Elementary time step.
    prob: float
        Probability of the particle moving in the X or Y axis.

    Returns
    -------
    xip1 : float
        Particle position in the X-axis
    yip1 : float
        Particle position in the Y-axis

    """
    eps = random.choice([-1, 1])
    A = random.random()
    xip1 = xi
    yip1 = yi
    if A < prob:
        xip1 = xi + eps * v * dt
    else:
        yip1 = yi + eps * v * dt
        
    return xip1, yip1
    
# Display
def plot_curve(x, y, xlabel="", ylabel="", legend="", title="",
                xlog=False, ylog=False, fignumber=0, clear=False, linewidth = 1):

    # Create or retrieve the figure
    plt.figure(fignumber, figsize=(10, 5.714))
    # Clear the current figure if needed
    if clear: plt.clf()
    # Display the curve and legend
    if legend:
        plt.plot(x,y, '.-',label=legend, linewidth = linewidth)
        plt.legend()
    else:
        plt.plot(x,y,'.-', linewidth = linewidth) # Line + points
    # Display the title if needed
    if title: plt.title(title)
    # Set log scale if needed
    if xlog: plt.xscale("log")
    if ylog: plt.yscale("log")
    # Display labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(linewidth=0.00001)
    # Display the graph
    #plt.show()

def plot_histogram(x, nbins, xlabel="", ylabel="", legend="", title="",
                xlog=False, ylog=False, fignumber=0, clear=False):

    # Create or retrieve the figure
    plt.figure(fignumber, figsize=(7, 5))
    # Clear the current figure if needed
    if clear: plt.clf()
    # Display the curve and legend
    if legend:
        plt.hist(x,bins=nbins,histtype='step',lw=2,label=legend)
        plt.legend()
    else:
        plt.hist(x,bins=nbins,histtype='step',lw=2)
    # Display the title if needed
    if title: plt.title(title)
    # Set log scale if needed
    if xlog: plt.xscale("log")
    if ylog: plt.yscale("log")
    # Display labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Display the graph
    #plt.show()

# Calculations
def calculate_mean_squared_displacement(xk):
    """
    Computes the mean squared displacement of the particles at time ti.

    Parameters
    ----------
    xk : Array
        Particle positions

    Returns
    -------
    sigma_carre : float
        Mean squared displacement of the particles
    """
    # Retrieve the total number of trajectories
    N = len(xk)
    sum = 0
    # Initialize the mean squared displacement
    for i in range(0, N):
        sum = sum + xk[i]**2
        
    sigma_carre = sum/(N)
    return sigma_carre
    

def calculate_mean_squared_displacement2D(xk, yk):
    """
    Parameters
    ----------
    xk : TYPE
        DESCRIPTION.
    yk : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # Retrieve the total number of trajectories
    N = len(xk)
    sum = 0
    # Initialize the mean squared displacement
    for i in range(0, N):
        sum = sum + xk[i]**2 + yk[i]**2
    sigma_carre = sum/(N)
    return sigma_carre