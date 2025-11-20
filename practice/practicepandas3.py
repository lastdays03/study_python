import pandas as pd
import numpy as np

# concat() 함수 샘플데이터 예제
def concat_example():
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

# join() 함수 샘플데이터 예제
def join_example():
    # df1과 df2의 인덱스를 일부 겹치고 일부 다르게 해서 조인 방식에 따라 결과가 다르게 나오도록 변경
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': ['a', 'b', 'c', 'd']
    }, index=['x', 'y', 'z', 'w'])
    print("\ndf1:")
    print(df1)
    df2 = pd.DataFrame({
        'C': [10, 20, 30],
        'D': ['p', 'q', 'r']
    }, index=['w', 'y', 'k'])  # 'y', 'w'는 겹치고, 'k'는 df1에 없음, 'x','z'는 df2에 없음
    print("\ndf2:")
    print(df2)
    result_join = df1.join(df2) # 기본 조인은 왼쪽 조인
    print("\ndf1.join(df2) 결과 (기본 조인):")
    print(result_join)
    result_join = df1.join(df2, how='inner') # 내부 조인은 겹치는 인덱스만 조인
    print("\ndf1.join(df2, how='inner') 결과 (내부 조인):")
    print(result_join)
    result_join_left = df1.join(df2, how='left') # 왼쪽 조인은 df1의 인덱스만 조인
    print("\ndf1.join(df2, how='left') 결과 (왼쪽 조인):")
    print(result_join_left)
    result_join_right = df1.join(df2, how='right') # 오른쪽 조인은 df2의 인덱스만 조인
    print("\ndf1.join(df2, how='right') 결과 (오른쪽 조인):")
    print(result_join_right)
    result_join_outer = df1.join(df2, how='outer') # 외부 조인은 df1과 df2의 모든 인덱스를 조인
    print("\ndf1.join(df2, how='outer') 결과 (외부 조인):")
    print(result_join_outer)

# merge() 함수 샘플데이터 예제
def merge_example():
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': ['a', 'b', 'c', 'd']
    }, index=['x', 'y', 'z', 'w'])
    print("\ndf1:")
    print(df1)
    df2 = pd.DataFrame({
        'A': [1, 2, 4],
        'C': [10, 20, 30],
        'D': ['p', 'q', 'r']
    }, index=['w', 'y', 'k'])
    print("\ndf2:")
    print(df2)
    result_merge = pd.merge(df1, df2, on='A') # 기본 조인은 내부 조인
    print("\npd.merge(df1, df2, on='A') 결과 (A 열을 기준으로 조인):")
    print(result_merge)
    result_merge = pd.merge(df1, df2, on='A', how='inner') # 내부 조인은 겹치는 인덱스만 조인
    print("\npd.merge(df1, df2, on='A', how='inner') 결과 (A 열을 기준으로 내부 조인):")
    print(result_merge)
    result_merge = pd.merge(df1, df2, on='A', how='left') # 왼쪽 조인은 df1의 인덱스만 조인
    print("\npd.merge(df1, df2, on='A', how='left') 결과 (A 열을 기준으로 왼쪽 조인):")
    print(result_merge)
    result_merge = pd.merge(df1, df2, on='A', how='right') # 오른쪽 조인은 df2의 인덱스만 조인
    print("\npd.merge(df1, df2, on='A', how='right') 결과 (A 열을 기준으로 오른쪽 조인):")
    print(result_merge)
    result_merge = pd.merge(df1, df2, on='A', how='outer') # 외부 조인은 df1과 df2의 모든 인덱스를 조인
    print("\npd.merge(df1, df2, on='A', how='outer') 결과 (A 열을 기준으로 외부 조인):")
    print(result_merge)

def main():
    while True:
        print("1. concat() 함수 샘플데이터 예제")
        print("2. join() 함수 샘플데이터 예제")
        print("3. merge() 함수 샘플데이터 예제")
        print("4. 종료")
        choice = input("원하는 함수를 선택하세요: ")
        if choice == '1':
            print("concat() 함수 샘플데이터 예제")
            concat_example()
            break
        elif choice == '2':
            print("join() 함수 샘플데이터 예제")
            join_example()
            break
        elif choice == '3':
            print("merge() 함수 샘플데이터 예제")
            merge_example()
            break
        elif choice == '4':
            print("종료합니다.")
            break
        else:   
            print("올바른 함수를 선택하세요.")
            continue

if __name__ == "__main__":
    main()
