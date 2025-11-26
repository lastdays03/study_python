import pandas as pd
import numpy as np

# 1. DataFrame 생성 (리스트의 리스트)
# 행 단위로 데이터 입력, 컬럼명 지정
df1 = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], columns=['A', 'B', 'C'])
print(df1)

# 2. DataFrame 생성 (딕셔너리)
# 키가 컬럼명이 되고, 값이 데이터가 됨
df2 = pd.DataFrame(
    {
        'A': ['a', 'b', 'c'],
        'B': ['d', 'e', 'f'],
        'C': ['g', 'h', 'i']
    }
)

# 3. DataFrame 생성 (딕셔너리 + 인덱스/컬럼 지정)
# 데이터 순서 지정 및 인덱스 설정
columns =['지역','2000','2005','2010','2015', '2010-2015 증가율']
index = ['서울','부산','인천','대구']
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}
df3 = pd.DataFrame(data, index=index, columns=columns)
print(df3)

# 4. DataFrame 생성 (Series 리스트)
# Series의 인덱스가 컬럼명이 됨 (매칭 안되면 NaN)
a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])

df4 = pd.DataFrame([a, b, c], index=['a', 'b', 'c'])
print(df4)

# 5. CSV 파일 읽기
# index_col: 인덱스로 사용할 컬럼 지정
# usecols: 불러올 컬럼 지정
train_data = pd.read_csv('data/train.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Name', 'Sex', 'Age'])
print(train_data)
print(train_data.info()) # 데이터프레임 정보 (타입, 결측치 등)
print(train_data.head()) # 상위 5개 행
print(train_data.columns) # 컬럼 목록
print(type(train_data.columns))
print(train_data.index) # 인덱스 목록
print(type(train_data.index))

# 6. 인덱스/컬럼 이름 설정
df4.index.name = 'index'
df4.columns.name = 'value'
print(df4)
print(type(df4.values)) # numpy array로 반환
print(df4.values)

# 7. 데이터프레임 속성 및 통계
print(train_data.head())
print(len(train_data)) # 행 개수
print(train_data.size) # 전체 원소 개수
print(train_data.shape) # (행, 열) 크기
print(train_data.describe()) # 기술 통계량 (수치형 데이터)

# 8. 전치 (Transpose)
# 행과 열을 바꿈
print(df3)
print(df3.T)
print(df3.T['서울'])
print(df3.T['서울']['2000'])
print(df3.columns)

# 9. 열 데이터 갱신 및 추가
# 기존 열 갱신
df3['2010-2015 증가율'] = df3['2010-2015 증가율'] * 100
print(df3)

# 새 열 추가
df3['비고'] = ['비고1', '비고2', '비고3', '비고4']
print(df3)

# 열 삭제 (del 키워드)
del df3['비고']
print(df3)

# 계산된 열 추가
df3['2005-2015 증가율'] = ((df3['2015'] - df3['2005']) / df3['2005'] * 100).round(2)
print(df3)
del df3['2005-2015 증가율']
print(df3)

# 10. 행 추가/수정 (loc)
df3.loc['광주'] = ['호남권', 2466052, 2456016, 2000002, 2466052, 1.00]
print(df3)

# 11. 열 선택 (Indexing)
# 단일 열 선택 (Series 반환)
print(df3['지역'])
print(type(df3['지역']))

# 속성으로 접근 (컬럼명이 식별자 규칙 따를 때)
print(df3.지역)
print(type(df3.지역))

# 리스트로 열 선택 (DataFrame 반환)
print(df3[['지역']])
print(type(df3[['지역']]))

# 여러 열 선택
print(df3[['2005', '2010']])
print(type(df3[['2005', '2010']]))

# 잘못된 인덱싱 (정수형 인덱스가 아닐 때 정수 키 사용 불가)
try:
    print(df3[0])
except Exception as e:
    print(e)

# 정수형 컬럼명을 가진 데이터프레임
df5 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df5)
print(df5[[1,2]]) # 컬럼 1, 2 선택

# 12. 행 선택 (Slicing)
# 라벨 슬라이싱 (끝 포함)
print(df3[:'인천'])
print(df3['인천':])
print(df3['인천':'인천'])

# 위치 슬라이싱 (끝 미포함)
print(df3[:2])
print(df3[2:])
print(df3[2:3])

# 13. 개별 데이터 접근
# 열 -> 행 순서
print(df3['2015']) # Series
print(df3['2015']['서울']) # 값

# DataFrame -> 행 슬라이싱
print(df3[['2015']]) # DataFrame
print(df3[['2015']]['부산':'부산']) # DataFrame

# 여러 열 -> 행 슬라이싱
print(df3[['2015', '2005']])
print(df3[['2015', '2005']]['부산':])

# 14. 데이터 삭제 (drop)
print(df3.head(2))

# 행 삭제 (원본 유지)
print(df3.drop(index=['광주']))
print(df3)

# 여러 행 삭제
print(df3.drop(index=['광주', '대구']))
print(df3)

# 행 삭제 (inplace=True, 원본 수정)
df3.drop(index=['광주'], inplace=True)
print(df3)

# 열 삭제 (columns 지정)
print(df3.drop(columns=['2010-2015 증가율', '2010']))
print(df3)

# axis 지정하여 삭제 (0: 행, 1: 열)
print(df3.drop(['대구'], axis=0))
print(df3.drop(columns=['2010-2015 증가율'], axis=1))
