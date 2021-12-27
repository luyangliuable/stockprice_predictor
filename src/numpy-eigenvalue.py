import numpy as np

inputs = np.array([[2, -1], [4, -2]])
w, v = np.linalg.eig(inputs)
print(inputs)
print(w)
print(v)


inputs = np.array([[2, -1], [4, 3]])
w, v = np.linalg.eig(inputs)

print(inputs)
print(w)
print(v)

