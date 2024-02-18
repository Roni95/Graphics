import matplotlib.pyplot as plt

def draw_circle_bresenham(center_x, center_y, radius):
    x = radius
    y = 0
    p = 1 - radius

    x_points, y_points = [], []

    while x >= y:
        x_points.append(x + center_x)
        y_points.append(y + center_y)
        x_points.append(y + center_x)
        y_points.append(x + center_y)
        x_points.append(-x + center_x)
        y_points.append(y + center_y)
        x_points.append(-y + center_x)
        y_points.append(x + center_y)

        if x != y:
            x_points.append(y + center_x)
            y_points.append(-x + center_y)
            x_points.append(x + center_x)
            y_points.append(-y + center_y)
            x_points.append(-y + center_x)
            y_points.append(-x + center_y)
            x_points.append(-x + center_x)
            y_points.append(-y + center_y)

        if p <= 0:
            y += 1
            p = p + 2*y + 1
        else:
            x -= 1
            y += 1
            p = p + 2*y - 2*x + 1

    return x_points, y_points

# User input for circle parameters
center_x = int(input("Enter center_x: "))
center_y = int(input("Enter center_y: "))
radius = int(input("Enter radius: "))

# Call the draw_circle_bresenham function
x_points, y_points = draw_circle_bresenham(center_x, center_y, radius)

# Plot the circle
plt.plot(x_points, y_points, marker='o', linestyle='None', markersize=1)
plt.title('Bresenham\'s Circle Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()