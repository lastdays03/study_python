# 파이썬 zip 함수와 언패킹(Unpacking) - 요약

> **참고**: 이 문서의 상세한 내용은 [리스트 컴프리헨션과 zip, 언패킹 조합 문법](./python_list_comprehension_zip.md) 문서에 통합되었습니다. 
> 
> 해당 문서에서 다음 내용을 확인할 수 있습니다:
> - 리스트 컴프리헨션 기본 개념 (섹션 1)
> - 언패킹(Unpacking) 개념 (섹션 2)
> - zip() 함수 개념 및 실전 활용 (섹션 3)
> - 리스트 컴프리헨션, 언패킹, zip 조합 (섹션 4-13)

## 빠른 참조

### zip() 함수 기본

```python
# 여러 이터러블을 병렬로 묶기
l1 = [1, 2, 3]
l2 = [4, 5, 6]
zipped = list(zip(l1, l2))  # [(1, 4), (2, 5), (3, 6)]
```

### 언패킹 기본

```python
# 튜플/리스트 언패킹
x, y = (3, 4)
a, b, c = [1, 2, 3]

# zip과 언패킹 조합
for x, y in zip(l1, l2):
    print(x, y)
```

### 실전 활용

```python
# 두 리스트를 딕셔너리로 변환
keys = ['name', 'age']
values = ['홍길동', 25]
person = dict(zip(keys, values))

# 리스트 전치
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))

# 리스트 컴프리헨션과 조합
students = [{'name': n, 'score': s} for n, s in zip(names, scores)]
```

자세한 내용과 예제는 [python_list_comprehension_zip.md](./python_list_comprehension_zip.md)를 참고하세요.
