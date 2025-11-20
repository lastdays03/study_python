import pandas as pd
import numpy as np

d1 = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 28],
    '직업': ['개발자', '디자이너', '개발자']
})
print("d1:\n", d1)
print("d1['이름']:\n", d1['이름'])
# print("d1.loc[0]:\n", d1.loc[0])
# print("d1.iloc[0]:\n", d1.iloc[0])
# print("d1.loc[0, '이름']:\n", d1.loc[0, '이름'])
# print("d1.iloc[0, 0]:\n", d1.iloc[0, 0])

d2 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']])
print("d2:\n", d2)

d3 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']], columns=['이름', '나이', '직업'])
print("d3:\n", d3)

d4 = pd.DataFrame([['홍길동', 25, '개발자'], ['김철수', 30, '디자이너'], ['이영희', 28, '개발자']], index=pd.date_range(start='2025-01-01', periods=3), columns=['이름', '나이', '직업'],)
print("d4:\n", d4)

d5 = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 28],
    '직업': ['개발자', '디자이너', '개발자']
}, index=pd.date_range(start='2025-01-01', periods=3))
print("d5:\n", d5)

d6 = pd.DataFrame(np.arange(12).reshape(4, 3), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C'])
print("d6:\n", d6)

d7 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print("d7:\n", d7)
print("d7['A']:\n", d7['A'])
print("d7.index:\n", d7.index)
print("d7.columns:\n", d7.columns)
print("d7.values:\n", d7.values)
print("d7.shape:\n", d7.shape)
print("d7.size:\n", d7.size)
print("d7.ndim:\n", d7.ndim)
print("d7['A'].dtype:\n", d7['A'].dtype)
print("d7.index.name:\n", d7.index.name)

d8 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
print("d8:\n", d8)
print("d8['A']:\n", d8['A'])
print("d8.A:\n", d8.A)
print("d8.index:\n", d8.index)
print("d8.columns:\n", d8.columns)
print("d8.values:\n", d8.values)

print("d6 + d7:\n", d6 + d7)
print("d7 + d8:\n", d7 + d8)

d9 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'C': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
})
print("d9:\n", d9)
print("d9.describe():\n", d9.describe())
print("d9.info():\n", d9.info())
print("d9.head():\n", d9.head())
print("d9.tail():\n", d9.tail())
print("d9.sample(n=2):\n", d9.sample(n=2))
print("d9.sample(n=2, random_state=1):\n", d9.sample(n=2, random_state=1))
print("d9.sample(n=2, random_state=2):\n", d9.sample(n=2, random_state=2))
print("d9.sample(n=2, random_state=3):\n", d9.sample(n=2, random_state=3))
print("d9.sample(n=2, random_state=4):\n", d9.sample(n=2, random_state=4))
print("d9.sample(n=2, random_state=5):\n", d9.sample(n=2, random_state=5))
print("d9[0:1]:\n", d9[0:1])
print("d9['A']: \n", d9['A'])
print("d9[1:3]:\n", d9[1:3])
print("d9.loc[1]: \n", d9.loc[1])
print("d9.loc[1:3]: \n", d9.loc[1:3])
print("d9.mean():\n", d9.mean())
print("d9.mean(axis=1):\n", d9.mean(axis=1))
print("d9.mean(axis=0):\n", d9.mean(axis=0))
print("d9.median():\n", d9.median())
print("d9.median(axis=1):\n", d9.median(axis=1))
print("d9.median(axis=0):\n", d9.median(axis=0))
print("d9.std():\n", d9.std())
print("d9.std(axis=1):\n", d9.std(axis=1))
print("d9.std(axis=0):\n", d9.std(axis=0))
print("d9.max():\n", d9.max())
print("d9.max(axis=1):\n", d9.max(axis=1))
print("d9.max(axis=0):\n", d9.max(axis=0))
print("d9.min():\n", d9.min())
print("d9.min(axis=1):\n", d9.min(axis=1))
print("d9.min(axis=0):\n", d9.min(axis=0))
print("d9.sum():\n", d9.sum())
print("d9.sum(axis=1):\n", d9.sum(axis=1))
print("d9.sum(axis=0):\n", d9.sum(axis=0))
print("d9.count():\n", d9.count())
print("d9.count(axis=1):\n", d9.count(axis=1))
print("d9.count(axis=0):\n", d9.count(axis=0))
print("d9.size:\n", d9.size)
print("d9.shape:\n", d9.shape)
print("d9.ndim:\n", d9.ndim)
print("d9.index:\n", d9.index)
print("d9.columns:\n", d9.columns)
print("d9.values:\n", d9.values)
print("d9.T:\n", d9.T)

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
