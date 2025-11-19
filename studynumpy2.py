import numpy as np

data1 = [1, 2, 3, 4, 5]
a1 = np.array(data1)
print("a1:", a1)

data2 = [0.1, 0.2, 0.3, 0.4, 10]
a2 = np.array(data2)
print("a2:", a2)

print("a1.dtype:", a1.dtype)
print("a2.dtype:", a2.dtype)

a3 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print("a3:", a3)

a4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print("a4:", a4)

a5 = np.arange(2, 10, 2)
print("a5:", a5)

a6 = np.arange(20).reshape(4, 5)
print("a6:", a6)
print("a6.shape:", a6.shape)

a7 = np.linspace(0, 10, 5)
print("a7:", a7)

a8 = np.linspace(0, np.pi, 10)
print("a8:", a8)
print("pi:", np.pi)

a9 = np.zeros((5,3))
print("a9:", a9)

a10 = np.ones((4,6))
print("a10:", a10)

a11 = np.eye(5)
print("a11:", a11)

a12 = np.diag([1, 2, 3, 4, 6])
print("a12:", a12)

a13 = np.array(['apple', 'banana', 'cherry'])
print("a13:", a13)
print("a13.dtype:", a13.dtype)

a14 = np.array(['1.2', '2.3', '3.4'])
print("a14:", a14)
print("a14.dtype:", a14.dtype)
a15 = a14.astype(np.float64)
print("a15:", a15)
print("a15.dtype:", a15.dtype)
# a16 = a14.astype(np.int32)
# print("a16:", a16)
# print("a16.dtype:", a16.dtype)

a16 = np.array(['1', '2', '3'])
print("a16:", a16)
print("a16.dtype:", a16.dtype)
a17 = a16.astype(np.int32)
print("a17:", a17)
print("a17.dtype:", a17.dtype)

a18 = np.array([1.22, 3.22, 4.23])
print("a18:", a18)
print("a18.dtype:", a18.dtype)
a19 = a18.astype(np.int32)
print("a19:", a19)
print("a19.dtype:", a19.dtype)

a20 = np.random.rand(5, 3, 4)
print("a20:", a20)
print("a20.dtype:", a20.dtype)

a21 = np.random.rand()
print("a21:", a21)
print("type(a21):", type(a21))

a22 = np.random.randint(0, 10, 5)
print("a22:", a22)

a23 = np.random.randint(10)
print("a23:", a23)

a24 = np.random.randint(0, 10)
print("a24:", a24)

a25 = np.random.randint(0, 10, (4, 3))
print("a25:", a25)

a26 = np.random.randint(0, 10, size=(4, 3, 2))
print("a26:", a26)

a27 = np.arange(24).reshape(4, 3, 2)
print("a27:", a27)
print("a27[1]:", a27[1])
print("a27[1, 2]:", a27[1, 2])
print("a27[1][2]:", a27[1][2])
print("a27[1, 2, 0]:", a27[1, 2, 0])
print("a27[1][2][0]:", a27[1][2][0])

a28 = np.arange(48).reshape(4, 3, 4)
print("a28:", a28)
print("a28[0:2]:", a28[0:2])
print("a28[0:2, 0:1]:", a28[0:2, 0:1])
print("a28[0:2][0:1]:", a28[0:2][0:1])
print("a28[0:2, 0:1, 0:2]:", a28[0:2, 0:1, 0:2])
print("a28[0:2][0:1][0:2]:", a28[0:2][0:1][0:2])

a29 = np.arange(24).reshape(4, 3, 2)
print("a29:", a29)
a30 = a29.reshape(6, 4)
print("a30:", a30)
a31 = a29.reshape(24)
print("a31:", a31)
a32 = a29.reshape(-1)
print("a32:", a32)
a33 = a30.reshape(-1)
print("a33:", a33)