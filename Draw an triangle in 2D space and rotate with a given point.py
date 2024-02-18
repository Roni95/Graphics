import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def rotate_point(point, center, angle):
    """Rotate a point around another point by a given angle."""
    angle_rad = np.radians(angle)
    x, y = point
    cx, cy = center
    new_x = (x - cx) * np.cos(angle_rad) - (y - cy) * np.sin(angle_rad) + cx
    new_y = (x - cx) * np.sin(angle_rad) + (y - cy) * np.cos(angle_rad) + cy
    return new_x, new_y

# Get triangle vertices from the user
triangle_vertices = []
for i in range(3):
    x = float(input(f"Enter x-coordinate of vertex {i+1}: "))
    y = float(input(f"Enter y-coordinate of vertex {i+1}: "))
    triangle_vertices.append([x, y])

# Convert to NumPy array
triangle = np.array(triangle_vertices)

# Get rotation center from the user
center_x = float(input("Enter x-coordinate of rotation center: "))
center_y = float(input("Enter y-coordinate of rotation center: "))
center = np.array([center_x, center_y])

# Get rotation angle from the user
angle = float(input("Enter rotation angle in degrees: "))

# Rotate triangle vertices
rotated_triangle = np.array([rotate_point(vertex, center, angle) for vertex in triangle])

# Plotting
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.add_patch(Polygon(triangle, color='b', alpha=0.5))
ax.add_patch(Polygon(rotated_triangle, color='r', alpha=0.5))
ax.plot(center[0], center[1], 'ko')  # Plot rotation center
ax.annotate('Rotation Center', xy=(center[0], center[1]), xytext=(center[0] + 0.1, center[1] + 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle Rotation')
plt.grid(True)
plt.show()