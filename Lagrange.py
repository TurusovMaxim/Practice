import matplotlib.pyplot as plt
import numpy as np
import re

a = []
b = []
points = open("Coordinates.txt", "r")
# reading all content from file
if points.mode == "r":
    read_points = points.read()
    print(read_points)
# file splitting into lines
for strings in read_points.split('\n'):
    x, y = (re.split(r'\s+', strings))
    a.append(float(x))
    b.append(float(y))
    coordinate_x = np.array(a, dtype=float)
    coordinate_y = np.array(b, dtype=float)


def lagrange(coordinate_x, coordinate_y, t):
    z = 0
    for j in range(len(coordinate_y)):
        p1 = 1;
        p2 = 1
        for i in range(len(coordinate_x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - coordinate_x[i])
                p2 = p2 * (coordinate_x[j] - coordinate_x[i])
        z = z + coordinate_y[j] * p1 / p2
    return z

# output
xnew=np.linspace(np.min(coordinate_x), np.max(coordinate_x), 100)
ynew=[lagrange(coordinate_x, coordinate_y, i) for i in xnew]
plt.plot(coordinate_x, coordinate_y, 'o', xnew, ynew)
plt.grid(True)
plt.show()

