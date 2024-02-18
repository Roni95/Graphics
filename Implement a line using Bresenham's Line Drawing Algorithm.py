import matplotlib.pyplot as plt

def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    # Lists to store the points
    x_points = []
    y_points = []
    
    while x0 != x1 or y0 != y1:
        # Plot the point (x0, y0)
        x_points.append(x0)
        y_points.append(y0)
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    # Add the last point
    x_points.append(x1)
    y_points.append(y1)

    return x_points, y_points

# Get input from the user
x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

# Call the draw_line function
x_points, y_points = draw_line(x0, y0, x1, y1)

# Plot the line
plt.plot(x_points, y_points, marker='o')
plt.title('Line Drawing')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()