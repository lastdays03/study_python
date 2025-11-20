import pandas as pd
import numpy as np

# append() 함수 샘플데이터 예제

# DataFrame 1 만들기
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})
print("df1:")
print(df1)

# DataFrame 2 만들기
df2 = pd.DataFrame({
    'A': [4, 5],
    'B': ['d', 'e']
})
print("\ndf2:")
print(df2)

# ⚠️ 참고: pandas 1.4.0 이후 append는 deprecated. concat 사용 권장.
# 판다스 2.2.3에서는 append()가 제거되었으므로 concat()을 사용하여 동일한 동작을 구현할 수 있습니다.

# DataFrame을 이어붙일 때는 concat() 사용
result_concat = pd.concat([df1, df2])
print("\npd.concat([df1, df2]) 결과 (인덱스 유지):")
print(result_concat)

result_concat_reset = pd.concat([df1, df2], ignore_index=True)
print("\npd.concat([df1, df2], ignore_index=True) 결과 (인덱스 재정렬):")
print(result_concat_reset)

# Series를 DataFrame에 추가하고 싶을 때도 concat 사용
row = pd.Series({'A': 6, 'B': 'f'})
row_df = pd.DataFrame([row])
df3_concat = pd.concat([df1, row_df], ignore_index=True)
print("\ndf1에 Series concat 결과:")
print(df3_concat)

# 열 방향으로 연결
result_concat_axis1 = pd.concat([df1, df2], axis=1)
print("\npd.concat([df1, df2], axis=1) 결과 (열 방향 연결):")
print(result_concat_axis1)
