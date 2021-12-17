import numpy as np

a = np.random.randint(0, 100, size=[5, 3])
print(a)
print('-------------')

b = np.random.randint(0, 100, size=[3, 2])
print(b)
print('-------------')

print(np.matmul(a, b))