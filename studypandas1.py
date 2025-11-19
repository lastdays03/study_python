import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 10])
print("s1:", s1)

s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("s2:", s2)
print("s2['b']:", s2['b'])
print("s2.index:", s2.index)
print("s2.values:", s2.values)
print("s2.dtype:", s2.dtype)
print("s2.shape:", s2.shape)
print("s2.size:", s2.size)
print("s2.ndim:", s2.ndim)
print("s2.name:", s2.name)
# print("s2.index:", s2.index)

# d1 = pd.DataFrame({
#     '이름': ['홍길동', '김철수', '이영희'],
#     '나이': [25, 30, 28],
#     '직업': ['개발자', '디자이너', '개발자']
# })
# print("d1:", d1)
# print("d1['이름']:", d1['이름'])
# print("d1.loc[0]:", d1.loc[0])
# print("d1.iloc[0]:", d1.iloc[0])
# print("d1.loc[0, '이름']:", d1.loc[0, '이름'])
# print("d1.iloc[0, 0]:", d1.iloc[0, 0])