import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ObjectiveFunctions import *



# Generate 2D input array
x = np.linspace(-5.12, 5.12, 50)
y = np.linspace(-5.12, 5.12, 50)
X, Y = np.meshgrid(x, y)

# Calculate the objective values
rastrigin = rastrigin_function(2, -5.12 , 5.12)
Z = np.apply_along_axis(rastrigin.objective_value, axis=1, arr=np.column_stack((X.ravel(), Y.ravel())))
Z = Z.reshape(X.shape)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Objective Value')
ax.set_title('Rastrigin Function in 3D')

plt.show()
