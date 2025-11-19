import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 10])
print("s1:", s1)

s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("s2:", s2)
print("s2['b']:", s2['b'])
print("s2[['a', 'c']]:", s2[['a', 'c']])
print("s2.index:", s2.index)
print("s2.values:", s2.values)
print("s2.dtype:", s2.dtype)
print("s2.shape:", s2.shape)
print("s2.size:", s2.size)
print("s2.ndim:", s2.ndim)
print("s2.name:", s2.name)

s3 = pd.Series({'apple': 3, 'banana': 5, 'orange': 2, 'pear': np.nan})
print("s3:", s3)
print("s3['apple']: ", s3['apple'])

s4 = pd.Series(np.arange(25), index=np.arange(1, 26))
print("s4:", s4)

s5 = pd.Series(np.arange(5), index=pd.date_range(start='2025-01-01', periods=5))
print("s5:", s5)

s6 = pd.Series(np.arange(5), index=pd.date_range(start='2025-01-01', periods=5, freq='W'))
print("s6:", s6)

s7 = pd.Series(np.arange(5), index=pd.date_range(end='2025-01-10', periods=5))
print("s7:", s7)

s8 = pd.Series(np.arange(5), index=pd.date_range(start='2025-01-01', end='2025-01-5'))
print("s8:", s8)

print("s7 + s8:", s7 + s8)
print("s6 + s8:", s6 + s8)

s9 = pd.Series([1, 2, 3, 4, 5])
print("s9:", s9)

s10 = pd.Series([10, 0, 12, 13, 14.5])
print("s10:", s10)

print("s9 + s10:", s9 + s10)
print("s9 - s10:", s9 - s10)
print("s9 * s10:", s9 * s10)
print("s9 / s10:", s9 / s10)
print("s9 // s10:", s9 // s10)
print("s9 % s10:", s9 % s10)
print("s9 ** s10:", s9 ** s10)
