import numpy as np

a = np.random.randint(0, 100, size=36)
print(a)
print('---------')

divisor = int(input("type number: "))

new = np.array([i / divisor for i in a])
print(new)
print('---------')

new2 = np.array([int(i / divisor) for i in a if i % divisor == 0])
print(new2)
