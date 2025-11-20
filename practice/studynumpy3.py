import numpy as np

a1 = np.array([1, 4, 9, 16, 25])

# 제곱근
print("np.sqrt(a1):", np.sqrt(a1))

# 지수
print("np.exp(a1):", np.exp(a1))

# 로그
print("np.log(a1):", np.log(a1))

# 삼각함수
print("np.sin(a1):", np.sin(a1))

# 절댓값
print("np.abs(a1):", np.abs(a1))

# 올림, 내림, 반올림
a2 = np.array([1.2, 2.7, 3.5, 4.9])
print("np.ceil(a2):", np.ceil(a2))
print("np.floor(a2):", np.floor(a2))
print("np.round(a2):", np.round(a2))

a3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("a3:", a3)

# 스칼라 브로드캐스팅
print("a3 + 10:", a3 + 10)

# 1차원 배열 브로드캐스팅
a4 = np.array([10, 20, 30, 40, 50])
print("a3 + a4:", a3 + a4)

# 열 벡터 브로드캐스팅
a5 = np.array([[10], [20]])
print("a3 + a5:", a3 + a5)

# reshape
a6 = np.arange(12)
print("a6:", a6)

# 3x4 배열로 변환
print("a6.reshape(3, 4):", a6.reshape(3, 4))
# -1 사용 (자동 계산)
# 마지막 차원은 자동 계산
print("a6.reshape(3, -1):", a6.reshape(3, -1))
print("a6.reshape(2, 2, 3):", a6.reshape(2, 2, 3))
print("a6.reshape(2, 2, -1):", a6.reshape(2, 2, -1))

# flatten과 ravel: 1차원으로 변환
a7 = a6.reshape(3, 4)

# flatten 새로운 배열 반환
print("a7.flatten():", a7.flatten())

# ravel 가능하면 뷰 반환 (더 효율적)
print("a7.ravel():", a7.ravel())

