# 파이썬 zip 함수와 언패킹(Unpacking)

## 1. zip() 함수 기본 개념

`zip()` 함수는 여러 개의 이터러블(리스트, 튜플 등)을 병렬로 묶어서 튜플의 이터레이터를 반환합니다.

### 기본 사용법

```python
# 기본 예제
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

# zip 객체 반환 (직접 출력하면 메모리 주소만 보임)
zipped = zip(l1, l2)
print(zipped)  # <zip object at 0x...>

# 리스트로 변환하여 확인
print(list(zipped))  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
```

### 중요 특징

#### 1. 가장 짧은 이터러블 길이에 맞춤

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8]
print(list(zip(l1, l2)))  # [(1, 4), (2, 5), (3, 6)] - 3개만!
```

#### 2. 여러 개의 이터러블 동시 처리 가능

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [11, 12, 13]
print(list(zip(l1, l2, l3)))  # [(1, 4, 11), (2, 5, 12), (3, 6, 13)]
```

## 2. 언패킹(Unpacking) 개념

언패킹은 컬렉션의 요소를 개별 변수로 풀어내는 것입니다.

### 기본 언패킹

```python
# 튜플 언패킹
point = (3, 4)
x, y = point
print(x, y)  # 3 4

# 리스트 언패킹
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3
```

### zip과 언패킹 조합

```python
# zip 결과를 언패킹하여 사용
l1 = [1, 2, 3]
l2 = [4, 5, 6]

for x, y in zip(l1, l2):
    print(f"x={x}, y={y}")
# 출력:
# x=1, y=4
# x=2, y=5
# x=3, y=6
```

### 언패킹 연산자 (*)

```python
# * 연산자로 나머지 요소 언패킹
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# 함수 인자로 언패킹
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # add(1, 2, 3)과 동일
print(result)  # 6
```

## 3. zip과 언패킹의 실전 활용

### 3.1 두 리스트를 딕셔너리로 변환

```python
keys = ['name', 'age', 'city']
values = ['홍길동', 25, '서울']
person = dict(zip(keys, values))
print(person)  # {'name': '홍길동', 'age': 25, 'city': '서울'}
```

### 3.2 리스트 전치(행과 열 바꾸기)

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

### 3.3 여러 리스트를 동시에 순회

```python
names = ['홍길동', '김철수', '이영희']
ages = [25, 30, 28]
cities = ['서울', '부산', '대구']

for name, age, city in zip(names, ages, cities):
    print(f"{name}은(는) {age}세이고 {city}에 살고 있습니다.")
```

### 3.4 zip으로 묶은 후 다시 분리하기

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]

zipped = list(zip(l1, l2))
print(zipped)  # [(1, 4), (2, 5), (3, 6)]

# 언패킹으로 다시 분리
unzipped_l1, unzipped_l2 = zip(*zipped)
print(list(unzipped_l1))  # [1, 2, 3]
print(list(unzipped_l2))  # [4, 5, 6]
```

### 3.5 딕셔너리와 zip 활용

```python
# 딕셔너리의 키와 값을 zip으로 묶기
d1 = {'a': 1, 'b': 2, 'c': 3}
print(list(zip(d1.keys(), d1.values())))  # [('a', 1), ('b', 2), ('c', 3)]

# items() 메서드와 동일한 결과
print(list(d1.items()))  # [('a', 1), ('b', 2), ('c', 3)]
```

## 4. 실전 예제

### 예제 1: 여러 리스트를 동시에 처리

```python
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = [11, 12, 13, 14, 15]

# zip으로 묶기
zipped = list(zip(l1, l2, l3))
print(zipped)  # [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]

# 언패킹하여 각 요소 출력
for i, j, k in zipped:
    print(i, j, k)
```

### 예제 2: 데이터 변환

```python
# 학생 정보를 리스트로 관리
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]

# 딕셔너리 리스트로 변환
students = [{'name': n, 'score': s} for n, s in zip(names, scores)]
print(students)
# [{'name': '홍길동', 'score': 85}, {'name': '김철수', 'score': 92}, {'name': '이영희', 'score': 78}]
```

## 5. 주의사항

### 5.1 zip 객체는 한 번만 사용 가능

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
zipped = zip(l1, l2)

print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]
print(list(zipped))  # [] - 이미 소비됨!

# 해결책: 리스트로 변환하여 저장
zipped_list = list(zip(l1, l2))
print(list(zipped_list))  # [(1, 4), (2, 5), (3, 6)]
print(list(zipped_list))  # [(1, 4), (2, 5), (3, 6)] - 재사용 가능
```

### 5.2 길이가 다른 경우 주의

```python
# 기본 zip은 짧은 길이에 맞춤
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8]
print(list(zip(l1, l2)))  # [(1, 4), (2, 5), (3, 6)] - 7, 8은 무시됨

# itertools.zip_longest 사용하면 긴 것에 맞춤
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue=0)))
# [(1, 4), (2, 5), (3, 6), (0, 7), (0, 8)]
```

### 5.3 빈 이터러블 처리

```python
# 빈 리스트와 zip하면 빈 결과 반환
l1 = []
l2 = [1, 2, 3]
print(list(zip(l1, l2)))  # []
```

## 6. 언패킹 고급 활용

### 6.1 중첩 언패킹

```python
# 중첩된 구조 언패킹
data = [(1, 2), (3, 4), (5, 6)]
for x, y in data:
    print(x, y)
```

### 6.2 딕셔너리 언패킹

```python
# 딕셔너리를 함수 인자로 언패킹
def greet(name, age, city):
    return f"{name}님은 {age}세, {city}에 거주합니다"

person = {'name': '홍길동', 'age': 25, 'city': '서울'}
print(greet(**person))  # 홍길동님은 25세, 서울에 거주합니다
```

### 6.3 언패킹과 리스트 컴프리헨션

```python
# zip과 언패킹을 리스트 컴프리헨션에서 활용
l1 = [1, 2, 3]
l2 = [4, 5, 6]
result = [x + y for x, y in zip(l1, l2)]
print(result)  # [5, 7, 9]
```

## 7. 요약

- **zip()**: 여러 이터러블을 병렬로 묶어 튜플의 이터레이터 생성
- **언패킹**: 컬렉션의 요소를 개별 변수로 분리
- **zip + 언패킹**: 여러 리스트를 동시에 순회하거나 변환할 때 유용
- **주의**: zip 객체는 한 번만 사용 가능, 길이가 다르면 짧은 것에 맞춤

