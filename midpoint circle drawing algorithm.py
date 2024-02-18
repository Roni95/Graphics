import matplotlib.pyplot as plt

def draw_circle_midpoint(x_center, y_center, radius):
    x_points, y_points = [], []

    x = radius
    y = 0
    p = 1 - radius

    while x >= y:
        x_points.append(x + x_center)
        y_points.append(y + y_center)
        x_points.append(y + x_center)
        y_points.append(x + y_center)
        x_points.append(-x + x_center)
        y_points.append(y + y_center)
        x_points.append(-y + x_center)
        y_points.append(x + y_center)
        x_points.append(-x + x_center)
        y_points.append(-y + y_center)
        x_points.append(-y + x_center)
        y_points.append(-x + y_center)
        x_points.append(x + x_center)
        y_points.append(-y + y_center)
        x_points.append(y + x_center)
        y_points.append(-x + y_center)

        y += 1

        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

    return x_points, y_points

# User input for circle parameters
x_center = int(input("Enter x-coordinate of the center: "))
y_center = int(input("Enter y-coordinate of the center: "))
radius = int(input("Enter the radius: "))

# Call the draw_circle_midpoint function
x_points, y_points = draw_circle_midpoint(x_center, y_center, radius)

# Plot the circle
plt.scatter(x_points, y_points, s=5, color='black')
plt.title('Midpoint Circle Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to be equal
plt.show()