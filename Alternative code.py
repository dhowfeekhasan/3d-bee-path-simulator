import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
a = 10
b = 28
c = 2.667

# Initial conditions
x0, y0, z0 = 0, 1, 1.05
initial_state = [x0, y0, z0]

# Time span
t_span = (0, 50)  # seconds
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Define the system of ODEs
def bee_dynamics(t, state):
    x, y, z = state
    dxdt = a * (y - b)
    dydt = b * x - y - x * z
    dzdt = x * y - c * z
    return [dxdt, dydt, dzdt]

# Solve ODE
solution = solve_ivp(bee_dynamics, t_span, initial_state, t_eval=t_eval, method='RK45')

# Extract results
x, y, z = solution.y

# Plot the 3D trajectory
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5, color='blue')
ax.set_title("Bee's Path in 3D Space")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_zlabel("Z Position")
plt.show()
