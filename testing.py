import numpy as np


points = np.random.rand(12, 2)
corner_index = np.array([0, 3, 6, 9])

print(points)
points[0] = (3, 5)
print(points[0])