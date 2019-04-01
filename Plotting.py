import matplotlib.pyplot as plt
import re

points = open("Coordinates.txt", "r")
if points.mode == "r":
    read_points = points.read()
    print(read_points)

for strings in read_points.split('\n'):
    x, y = (re.split(r'\s+', strings))
    x = float(x)
    y = float(y)
    plt.scatter(x, y, color='blue')
plt.xlabel('X', fontsize=15)
plt.ylabel('Y', fontsize=15)
plt.title('Plotting', fontsize=15)
plt.show()
