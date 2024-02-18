import matplotlib.pyplot as plt

def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x, y = x1, y1
    x_points, y_points = [x], [y]
    
    for _ in range(int(steps)):
        x += x_increment
        y += y_increment
        x_rounded, y_rounded = round(x), round(y)
        x_points.append(x_rounded)
        y_points.append(y_rounded)
    
    return x_points, y_points

# User input for line coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Call the draw_line_dda function
x_points, y_points = draw_line_dda(x1, y1, x2, y2)

# Plot the line
plt.plot(x_points, y_points, marker='o')
plt.title('DDA Line Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()