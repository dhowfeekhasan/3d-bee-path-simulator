# Import necessary libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Define the Lorenz system of differential equations
# This function defines the "rules" of the Bee's movement.
# 'state' is a vector [x, y, z] and 't' is time.
def lorenz_system(state, t, a, b, c):
    """
    Calculates the derivatives for the Lorenz system.

    Args:
        state (list or array): The current state vector [x, y, z].
        t (float): The current time (required by odeint, but not used in these equations).
        a, b, c (float): The parameters of the system.

    Returns:
        list: The derivatives [dx/dt, dy/dt, dz/dt].
    """
    x, y, z = state
    
    # The Lorenz equations
    dx_dt = a * (y - x)
    dy_dt = x * (b - z) - y
    dz_dt = x * y - c * z
    
    return [dx_dt, dy_dt, dz_dt]

# 2. Set the parameters and initial conditions
# These are the values given in the problem description.
a = 10.0
b = 28.0
c = 2.667

# Initial position of the Bee in 3D space
initial_state = [0.0, 1.0, 1.05]

# 3. Create the time vector
# We need to define the time interval over which to solve the system.
# We'll solve from t=0 to t=40 with 10,000 points for a smooth curve.
t_start = 0
t_end = 40
num_points = 10000
t = np.linspace(t_start, t_end, num_points)

# 4. Solve the system of ODEs
# We use SciPy's 'odeint' function to integrate the lorenz_system.
# It takes our function, initial state, time points, and parameters as input.
# It returns an array with the [x, y, z] positions at each point in time.
solution = odeint(lorenz_system, initial_state, t, args=(a, b, c))

# Extract the individual x, y, and z coordinates from the solution
x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]

# 5. Plot the 3D trajectory (the Bee's path)
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the path with a color gradient over time to show direction
ax.plot(x, y, z, color='purple', alpha=0.7, linewidth=0.8)

# Add titles and labels for clarity
ax.set_title("Path of the Bee: The Lorenz Attractor")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Improve the viewing angle
ax.view_init(30, 60)

# Display the plot
plt.show()
