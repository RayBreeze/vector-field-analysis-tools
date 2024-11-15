"""
Curl Visualization Script

This script visualizes the curl of a vector field.

Made with love by Samman ;)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x_vals, y_vals, z_vals = np.meshgrid(np.linspace(-2, 2, 10),
                                     np.linspace(-2, 2, 10),
                                     np.linspace(-2, 2, 10))


Ax = y_vals * z_vals  
Ay = x_vals * z_vals  
Az = x_vals * y_vals 


div_A = np.gradient(Ax, axis=0) + np.gradient(Ay, axis=1) + np.gradient(Az, axis=2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

div_colors = div_A.flatten() 
sc = ax.scatter(x_vals.flatten(), y_vals.flatten(), z_vals.flatten(),
                c=div_colors, cmap='viridis')


plt.colorbar(sc, label='Divergence')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of the Divergence of A = yz i + xz j + xy k')

plt.show()
