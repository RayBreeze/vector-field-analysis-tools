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

curl_x = np.gradient(Az, axis=1) - np.gradient(Ay, axis=2)
curl_y = np.gradient(Ax, axis=2) - np.gradient(Az, axis=0)
curl_z = np.gradient(Ay, axis=0) - np.gradient(Ax, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(x_vals, y_vals, z_vals, curl_x, curl_y, curl_z, length=0.2, normalize=True)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of the Curl of the Vector Field A = yz i + xz j + xy k')

plt.show()