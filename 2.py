import numpy as np

n1 = np.random.randint(0, 100, 36)
print(n1)
print('-----------------')

n2 = n1.reshape(2, 18)
print(n2)
print('-----------------')

n3 = n1.reshape(3, 12)
print(n3)
print('-----------------')

n4 = n1.reshape(4, 9)
print(n4)
print('------------------')

n5 = n1.reshape(6, 6)
print(n5)
print('------------------')

n6 = n1.reshape(3, 3, 4)
print(n6)
print('-------------------')

n7 = n1.reshape(2, 3, 6)
print(n7)
print('-------------------')

n8 = n1.reshape(2, 9, 2)
print(n8)