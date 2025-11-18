import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6])
print(a1)
print(type(a1))
print(a1.dtype)
a11 = a1.reshape(3, 2)
print(a11)
print(a11[0, 1])
print(a11.shape)

# a2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(a2)
# print(type(a2))
# print(a2.dtype)
# print(a2.reshape(2, 5))


# a3 = np.arange(10, 20, 3)
# print(a3)
# print(type(a3))
# print(a3.dtype)
# print(a3.reshape(3, 3))
