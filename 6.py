import numpy as np

a = np.random.randint(0, 100, size=6)
print(a)
print('-------')

b = np.random.randint(0, 100, 9)
print(b)
print('--------')

c = np.random.randint(0, 100, 12)
print(c)
print('--------')

print(np.concatenate((a, b, c), axis=None))
