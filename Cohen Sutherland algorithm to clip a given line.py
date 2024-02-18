import matplotlib.pyplot as plt

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def computeCode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    clipped_points = [(x1, y1)]  # Store the initial point

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)
                clipped_points.append((x1, y1))  # Store the clipped point
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)
                clipped_points.append((x2, y2))  # Store the clipped point

    if accept:
        print("Line accepted from ({},{}) to ({},{})".format(x1, y1, x2, y2))
    else:
        print("Line rejected")

    return clipped_points

# Get input from the user for the coordinates of the line segment
x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))

# Get input from the user for window boundaries
xmin = int(input("Enter the minimum x-coordinate of the clipping window: "))
ymin = int(input("Enter the minimum y-coordinate of the clipping window: "))
xmax = int(input("Enter the maximum x-coordinate of the clipping window: "))
ymax = int(input("Enter the maximum y-coordinate of the clipping window: "))

# Example usage
clipped_points = cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# Unzip the clipped points
x_points, y_points = zip(*clipped_points)

# Plot the clipped line
plt.plot(x_points, y_points, marker='o')
plt.title('Cohen-Sutherland Line Clipping')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()