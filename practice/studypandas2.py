import pandas as pd
import numpy as np

d1 = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 28],
    '직업': ['개발자', '디자이너', '개발자']
})
print("d1:\n", d1)
#     이름  나이    직업
# 0  홍길동  25   개발자
# 1  김철수  30  디자이너
# 2  이영희  28   개발자
print("d1['이름']:\n", d1['이름'])
# 0    홍길동
# 1    김철수
# 2    이영희
# Name: 이름, dtype: object
print("d1.loc[0]:\n", d1.loc[0])
# 이름    홍길동
# 나이     25
# 직업    개발자
# Name: 0, dtype: object
print("d1.iloc[0]:\n", d1.iloc[0])
# 이름    홍길동
# 나이     25
# 직업    개발자
# Name: 0, dtype: object
print("d1.loc[0, '이름']:\n", d1.loc[0, '이름'])
# 홍길동
print("d1.iloc[0, 0]:\n", d1.iloc[0, 0])
# 홍길동

d2 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']])
print("d2:\n", d2)
#      0   1     2
# 0  홍길동  25   개발자
# 1  김철수  30  디자이너
# 2  이영희  28   개발자

d3 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']], columns=['이름', '나이', '직업'])
print("d3:\n", d3)
#     이름  나이    직업
# 0  홍길동  25   개발자
# 1  김철수  30  디자이너
# 2  이영희  28   개발자

d4 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']], index=pd.date_range(start='2025-01-01', periods=3), columns=['이름', '나이', '직업'],)
print("d4:\n", d4)
#              이름  나이    직업
# 2025-01-01  홍길동  25   개발자
# 2025-01-02  김철수  30  디자이너
# 2025-01-03  이영희  28   개발자

d5 = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 28],
    '직업': ['개발자', '디자이너', '개발자']
}, index=pd.date_range(start='2025-01-01', periods=3))
print("d5:\n", d5)
#              이름  나이    직업
# 2025-01-01  홍길동  25   개발자
# 2025-01-02  김철수  30  디자이너
# 2025-01-03  이영희  28   개발자

d6 = pd.DataFrame(np.arange(12).reshape(4, 3), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C'])
print("d6:\n", d6)
#    A   B   C
# a  0   1   2
# b  3   4   5
# c  6   7   8
# d  9  10  11

d7 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print("d7:\n", d7)
#    A  B   C   D
# a  0  1   2   3
# b  4  5   6   7
# c  8  9  10  11
print("d7['A']:\n", d7['A'])
# a    0
# b    4
# c    8
# Name: A, dtype: int64
print("d7.index:\n", d7.index)
# Index(['a', 'b', 'c'], dtype='object')
print("d7.columns:\n", d7.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')
print("d7.values:\n", d7.values)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print("d7.shape:\n", d7.shape)
# (3, 4)
print("d7.size:\n", d7.size)
# 12
print("d7.ndim:\n", d7.ndim)
# 2
print("d7['A'].dtype:\n", d7['A'].dtype)
# int64
print("d7.index.name:\n", d7.index.name)
# None

d8 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
print("d8:\n", d8)
#    A  B   C   D
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
print("d8['A']:\n", d8['A'])
# 0    0
# 1    4
# 2    8
# Name: A, dtype: int64
print("d8.A:\n", d8.A)
# 0    0
# 1    4
# 2    8
# Name: A, dtype: int64
print("d8.index:\n", d8.index)
# RangeIndex(start=0, stop=3, step=1)
print("d8.columns:\n", d8.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')
print("d8.values:\n", d8.values)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print("d6 + d7:\n", d6 + d7)
#       A     B     C   D
# a   0.0   2.0   4.0 NaN
# b   7.0   9.0  11.0 NaN
# c  14.0  16.0  18.0 NaN
# d   NaN   NaN   NaN NaN
print("d7 + d8:\n", d7 + d8)
#     A   B   C   D
# a NaN NaN NaN NaN
# b NaN NaN NaN NaN
# c NaN NaN NaN NaN
# 0 NaN NaN NaN NaN
# 1 NaN NaN NaN NaN
# 2 NaN NaN NaN NaN

d9 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'C': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
})
print("d9:\n", d9)
#     A    B     C
# 0   1   10   100
# 1   2   20   200
# 2   3   30   300
# 3   4   40   400
# 4   5   50   500
# 5   6   60   600
# 6   7   70   700
# 7   8   80   800
# 8   9   90   900
# 9  10  100  1000
print("d9.describe():\n", d9.describe())
#               A           B            C
# count  10.00000   10.000000    10.000000
# mean    5.50000   55.000000   550.000000
# std     3.02765   30.276504   302.765035
# min     1.00000   10.000000   100.000000
# 25%     3.25000   32.500000   325.000000
# 50%     5.50000   55.000000   550.000000
# 75%     7.75000   77.500000   775.000000
# max    10.00000  100.000000  1000.000000
print("d9.info():\n", d9.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   A       10 non-null     int64
#  1   B       10 non-null     int64
#  2   C       10 non-null     int64
# dtypes: int64(3)
# memory usage: 372.0 bytes
# d9.info():
#  None
print("d9.head():\n", d9.head())
#    A   B    C
# 0  1  10  100
# 1  2  20  200
# 2  3  30  300
# 3  4  40  400
# 4  5  50  500
print("d9.tail():\n", d9.tail())
#     A    B     C
# 5   6   60   600
# 6   7   70   700
# 7   8   80   800
# 8   9   90   900
# 9  10  100  1000
print("d9.sample(n=2):\n", d9.sample(n=2))
#     A    B     C
# 1   2   20   200
# 9  10  100  1000
print("d9.sample(n=2, random_state=1):\n", d9.sample(n=2, random_state=1))
#     A    B     C
# 2   3   30   300
# 9  10  100  1000
print("d9.sample(n=2, random_state=2):\n", d9.sample(n=2, random_state=2))
#    A   B    C
# 4  5  50  500
# 1  2  20  200
print("d9.sample(n=2, random_state=3):\n", d9.sample(n=2, random_state=3))
#    A   B    C
# 5  6  60  600
# 4  5  50  500
print("d9.sample(n=2, random_state=4):\n", d9.sample(n=2, random_state=4))
#    A   B    C
# 3  4  40  400
# 8  9  90  900
print("d9.sample(n=2, random_state=5):\n", d9.sample(n=2, random_state=5))
#     A    B     C
# 9  10  100  1000
# 5   6   60   600
print("d9[0:1]:\n", d9[0:1])
#    A   B    C
# 0  1  10  100
print("d9['A']: \n", d9['A'])
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9    10
# Name: A, dtype: int64
print("d9[1:3]:\n", d9[1:3])
#    A   B    C
# 1  2  20  200
# 2  3  30  300
print("d9.loc[1]: \n", d9.loc[1])
# A      2
# B     20
# C    200
# Name: 1, dtype: int64
print("d9.loc[1:3]: \n", d9.loc[1:3])
#    A   B    C
# 1  2  20  200
# 2  3  30  300
# 3  4  40  400
print("d9.mean():\n", d9.mean())
# A      5.5
# B     55.0
# C    550.0
# dtype: float64
print("d9.mean(axis=1):\n", d9.mean(axis=1))
# 0     37.0
# 1     74.0
# 2    111.0
# 3    148.0
# 4    185.0
# 5    222.0
# 6    259.0
# 7    296.0
# 8    333.0
# 9    370.0
# dtype: float64
print("d9.mean(axis=0):\n", d9.mean(axis=0))
# A      5.5
# B     55.0
# C    550.0
# dtype: float64
print("d9.median():\n", d9.median())
# A      5.5
# B     55.0
# C    550.0
# dtype: float64
print("d9.median(axis=1):\n", d9.median(axis=1))
# 0     10.0
# 1     20.0
# 2     30.0
# 3     40.0
# 4     50.0
# 5     60.0
# 6     70.0
# 7     80.0
# 8     90.0
# 9    100.0
# dtype: float64
print("d9.median(axis=0):\n", d9.median(axis=0))
# A      5.5
# B     55.0
# C    550.0
# dtype: float64
print("d9.std():\n", d9.std())
# A      3.027650
# B     30.276504
# C    302.765035
# dtype: float64
print("d9.std(axis=1):\n", d9.std(axis=1))
# 0     54.744863
# 1    109.489726
# 2    164.234588
# 3    218.979451
# 4    273.724314
# 5    328.469177
# 6    383.214039
# 7    437.958902
# 8    492.703765
# 9    547.448628
# dtype: float64
print("d9.std(axis=0):\n", d9.std(axis=0))
# A      3.027650
# B     30.276504
# C    302.765035
# dtype: float64
print("d9.max():\n", d9.max())
# A      10
# B     100
# C    1000
# dtype: int64
print("d9.max(axis=1):\n", d9.max(axis=1))
# 0     100
# 1     200
# 2     300
# 3     400
# 4     500
# 5     600
# 6     700
# 7     800
# 8     900
# 9    1000
# dtype: int64
print("d9.max(axis=0):\n", d9.max(axis=0))
# A      10
# B     100
# C    1000
# dtype: int64
print("d9.min():\n", d9.min())
# A      1
# B     10
# C    100
# dtype: int64
print("d9.min(axis=1):\n", d9.min(axis=1))
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9    10
# dtype: int64
print("d9.min(axis=0):\n", d9.min(axis=0))
# A      1
# B     10
# C    100
# dtype: int64
print("d9.sum():\n", d9.sum())
# A      55
# B     550
# C    5500
# dtype: int64
print("d9.sum(axis=1):\n", d9.sum(axis=1))
# 0     111
# 1     222
# 2     333
# 3     444
# 4     555
# 5     666
# 6     777
# 7     888
# 8     999
# 9    1110
# dtype: int64
print("d9.sum(axis=0):\n", d9.sum(axis=0))
# A      55
# B     550
# C    5500
# dtype: int64
print("d9.count():\n", d9.count())
# A    10
# B    10
# C    10
# dtype: int64
print("d9.count(axis=1):\n", d9.count(axis=1))
# 0    3
# 1    3
# 2    3
# 3    3
# 4    3
# 5    3
# 6    3
# 7    3
# 8    3
# 9    3
# dtype: int64
print("d9.count(axis=0):\n", d9.count(axis=0))
# A    10
# B    10
# C    10
# dtype: int64
print("d9.size:\n", d9.size)
# 30
print("d9.shape:\n", d9.shape)
# (10, 3)
print("d9.ndim:\n", d9.ndim)
# 2
print("d9.index:\n", d9.index)
# RangeIndex(start=0, stop=10, step=1)
print("d9.columns:\n", d9.columns)
# Index(['A', 'B', 'C'], dtype='object')
print("d9.values:\n", d9.values)
# [[   1   10  100]
#  [   2   20  200]
#  [   3   30  300]
#  [   4   40  400]
#  [   5   50  500]
#  [   6   60  600]
#  [   7   70  700]
#  [   8   80  800]
#  [   9   90  900]
#  [  10  100 1000]]
print("d9.T:\n", d9.T)
#      0    1    2    3    4    5    6    7    8     9
# A    1    2    3    4    5    6    7    8    9    10
# B   10   20   30   40   50   60   70   80   90   100
# C  100  200  300  400  500  600  700  800  900  1000

# 표준편차(standard deviation)의 공식: 
# 표본 표준편차(s), N개 데이터(x1, x2, ..., xN), 평균 mu = (x1 + ... + xN) / N
# s = sqrt( (1/(N-1)) * sum_{i=1}^{N} (xi - mu)**2 )
#
# Pandas의 std()는 ddof=1이 기본값(표본 표준편차)!
# 아래는 수식을 직접 계산해보는 예
# values = d9['A'].values
# mean = values.mean()
# variance = ((values - mean) ** 2).sum() / (len(values) - 1)  # ddof=1
# std = np.sqrt(variance)
# print("직접 계산한 표준편차(A열):", std)
# print("pandas 표준편차(A열):", d9['A'].std())
