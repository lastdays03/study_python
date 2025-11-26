import pandas as pd
import numpy as np

# 1. Series 생성 (리스트)
# 정수형 리스트로 생성
s1 = pd.Series([1, 3, 5])
print(s1)

# 2. Series 생성 (튜플)
# 실수형 튜플로 생성
s2 = pd.Series((1.0, 3.0, 5.0))
print(s2)

# 3. Series 생성 (문자열 리스트)
s3 = pd.Series(['a', 'b', 'c'])
print(s3)

# 4. Series 생성 (혼합 타입)
# 다양한 타입이 섞여 있으면 object 타입으로 생성됨
s4 = pd.Series(['a', 1, 3])
print(s4)

# 5. Series 생성 (range)
# range 객체로 생성
s5 = pd.Series(range(10, 14))
print(s5)

print(range(10, 14))

# 6. Series 생성 (numpy array)
# numpy arange로 생성
print(np.arange(100, 200, 5))

s6 = pd.Series(np.arange(100, 200, 5))
print(s6)

# 7. 결측치(NaN) 포함 Series
# NaN이 포함되면 float 타입으로 변환됨
s7 = pd.Series([1, 2, 3, np.nan, 6, 8])
print(s7)
print(s7.index)  # 인덱스 확인
print(s7.values) # 값 확인

# 8. 인덱스 지정하여 Series 생성
s8 = pd.Series([1, 2, 3, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s8)
print(s8.index)
print(s8.values)

# 인덱스 이름과 Series 이름 설정
s8.index.name = 'index'
print(s8)
s8.name = 'value'
print(s8)

# 9. 인덱싱 및 슬라이싱
# 라벨 인덱싱
print(s8['a'])
# 위치 인덱싱과 라벨 인덱싱 혼용
print(s8[0], s8['b'])
t1 = s8[0], s8['b']
print(t1)

# 위치 슬라이싱 (끝 미포함)
print(s8[1:4])
# 팬시 인덱싱 (여러 개 선택)
print(s8[['a', 'b']])
# 라벨 슬라이싱 (끝 포함)
print(s8['a':'c'])
# 속성처럼 접근 (라벨이 식별자 규칙을 따를 때)
print(s8.c)

# 10. 정수형 인덱스
s9 = pd.Series([1, 2, 3, np.nan, 6, 8], index=[1, 2, 3, 4, 5, 6])
print(s9)
# 팬시 인덱싱
print(s9[[1,3,4]])
# 위치 슬라이싱 (정수형 인덱스라도 슬라이싱은 위치 기반)
print(s9[0:4])

# 11. 연산
# 브로드캐스팅 (모든 원소에 5 더하기)
print(s9 + 5)

# 대용량 데이터 생성 및 연산
s10 = pd.Series(np.arange(10000000, 20000000, 1000000))
print(s10 / 10000000)

# 불리언 인덱싱 (조건 필터링)
print(s10[(s10 > 13000000) & (s10 < 17000000)])
print(s10 > 15000000) # 불리언 마스크 생성

# 인덱스 조건 검색
print(s10.index > 5)
print(s10[s10.index > 5])

# 조건 만족하는 개수 및 합계
print((s10 > 15000000).sum())
print(s10[(s10 > 14000000) & (s10 < 17000000)].sum())

# Series 간 연산 (인덱스 기준 정렬 후 연산, 매칭 안되면 NaN)
print(s10 + s9)

# 인덱스가 다른 두 Series 연산
s11 = pd.Series(np.arange(3000000, 4000000, 100000), index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s11)
# 인덱스 매칭 연산
print(s10 + s11)
# 값(values)만 추출하여 연산 (numpy array 연산, 순서대로)
print(s10.values + s11.values)

# 12. 포함 여부 확인 (in 연산자)
# 인덱스에 포함되어 있는지 확인
print(1 not in s10)
print(1 not in s11)

# 13. 아이템 순회
print(s11.items())
print(list(s11.items()))

for idx, value in s11.items():
    print(f"{idx} : {value}")

# 14. 딕셔너리로 Series 생성
scores = {'국어': 80, '영어': 90, '과학': 85, '수학': 95}
s12 = pd.Series(scores, index=scores.keys())
print(s12)

# 인덱스 순서 지정
s13 = pd.Series(scores, index=['국어', '수학', '영어', '과학'])
print(s13)

# 값 수정
s13['국어'] = 85
print(s13)

# 값 추가
s13['음악'] = 90
print(s13)

# 값 삭제
del s13['음악']
print(s13)

# 15. 통계 및 속성 함수
s14 = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.nan])
print(s14)
print(len(s14))      # 길이
print(s14.size)      # 전체 원소 수 (NaN 포함)
print(s14.count())   # 유효한 값 수 (NaN 제외)
print(s14.shape)     # 차원
print(s14.unique())  # 고유값
print(s14.mean())    # 평균
print(s14.median())  # 중앙값
print(s14.mode())    # 최빈값
print(s14.value_counts()) # 값별 빈도수

# 16. 날짜 범위 생성 (date_range)
# 일(day) 단위
index_date = pd.date_range(start='20230101', periods=15, freq='d')
print(index_date)

# 3일 단위
index_date = pd.date_range(start='20230101', periods=15, freq='3d')
print(index_date)

# 주(week) 단위 (일요일 기준)
index_date = pd.date_range(start='20230101', periods=15, freq='w')
print(index_date)

# 주(week) 단위 (월요일 기준)
index_date = pd.date_range(start='20230101', periods=15, freq='w-mon')
print(index_date)

# 월(Month) 단위 (월말 기준)
index_date = pd.date_range(start='20230101', periods=15, freq='M')
print(index_date)

# 월(Month) 단위 (월초 기준)
index_date = pd.date_range(start='20230101', periods=15, freq='MS')
print(index_date)

# 업무일(Business Month) 단위 (2개월 간격)
index_date = pd.date_range(start='20230101', periods=15, freq='2BM')
print(index_date)

# 분기(Quarter) 단위 (분기 초)
index_date = pd.date_range(start='20230101', periods=15, freq='QS')
print(index_date)
