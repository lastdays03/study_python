# 파이썬 클래스 기본

## 1. 클래스 기본 구조

```python
class ClassName:
    """클래스 설명"""
    
    # 클래스 변수 (모든 인스턴스가 공유)
    class_variable = "공유 변수"
    
    # 생성자
    def __init__(self, param1, param2):
        # 인스턴스 변수 (각 인스턴스마다 독립적)
        self.param1 = param1
        self.param2 = param2
    
    # 인스턴스 메서드
    def instance_method(self):
        return "인스턴스 메서드"
```

## 2. 클래스 변수 vs 인스턴스 변수

```python
class Person:
    # 클래스 변수
    species = "Homo sapiens"
    count = 0
    
    def __init__(self, name: str, age: int):
        # 인스턴스 변수
        self.name = name
        self.age = age
        Person.count += 1
    
    def get_info(self) -> str:
        return f"{self.name} ({self.age}세)"

# 사용 예시
person1 = Person("홍길동", 25)
person2 = Person("김철수", 30)

print(person1.species)  # "Homo sapiens" (클래스 변수)
print(person2.species)  # "Homo sapiens" (클래스 변수)
print(Person.count)     # 2 (생성된 인스턴스 수)

# 클래스 변수 변경
Person.species = "Human"
print(person1.species)  # "Human"
```

## 3. 생성자 (Constructor) - `__init__`

### 기본 생성자

```python
class Person:
    def __init__(self, name: str, age: int):
        """
        생성자 메서드
        self: 인스턴스 자신 (자동으로 전달됨)
        """
        self.name = name
        self.age = age
        # 리턴값 없음 (None 반환, 명시적으로 return 불필요)
```

### 기본값이 있는 생성자

```python
class Person:
    def __init__(self, name: str, age: int = 0, city: str = "서울"):
        """
        기본값이 있는 파라미터
        """
        self.name = name
        self.age = age
        self.city = city

# 사용 예시
person1 = Person("홍길동")  # age=0, city="서울" 사용
person2 = Person("김철수", 25)  # city="서울" 사용
person3 = Person("이영희", 30, "부산")  # 모든 값 지정
```

### 가변 파라미터

```python
class Config:
    def __init__(self, name: str, *args, **kwargs):
        """
        *args: 위치 인자들의 튜플
        **kwargs: 키워드 인자들의 딕셔너리
        """
        self.name = name
        self.args = args  # 튜플로 저장
        self.kwargs = kwargs  # 딕셔너리로 저장

# 사용 예시
config = Config("test", "arg1", "arg2", key1="value1", key2="value2")
```

### 타입 힌팅이 포함된 생성자

```python
from typing import Optional, List, Dict

class Student:
    def __init__(
        self,
        name: str,
        age: int,
        scores: Optional[List[int]] = None,
        info: Optional[Dict[str, str]] = None
    ) -> None:
        """
        타입 힌팅을 사용한 생성자
        -> None: 리턴값이 없음을 명시
        """
        self.name = name
        self.age = age
        self.scores = scores if scores is not None else []
        self.info = info if info is not None else {}
```

## 4. 인스턴스 메서드

```python
class Calculator:
    def __init__(self, value: int = 0):
        self.value = value
    
    def add(self, num: int) -> int:
        """인스턴스 메서드"""
        self.value += num
        return self.value
    
    def subtract(self, num: int) -> int:
        """빼기 메서드"""
        self.value -= num
        return self.value
    
    def get_value(self) -> int:
        """현재 값 반환"""
        return self.value
    
    def reset(self) -> None:
        """값 초기화 (리턴값 없음)"""
        self.value = 0

# 사용 예시
calc = Calculator(10)
calc.add(5)  # 15
calc.subtract(3)  # 12
print(calc.get_value())  # 12
```

## 5. 접근 제어자 (Access Modifiers)

### 공개 (Public)

```python
class MyClass:
    def __init__(self):
        self.public_var = "공개 변수"
    
    def public_method(self):
        """공개 메서드 (외부에서 자유롭게 접근 가능)"""
        return "public"
```

### 보호 (Protected)

```python
class MyClass:
    def __init__(self):
        self._protected_var = "보호 변수"
    
    def _protected_method(self):
        """
        보호 메서드 (관례적으로 내부 사용)
        _ 단일 언더스코어로 시작
        실제로는 접근 가능하지만 내부 사용 권장
        """
        return "protected"
```

### 비공개 (Private)

```python
class MyClass:
    def __init__(self):
        self.__private_var = "비공개 변수"
    
    def __private_method(self):
        """
        비공개 메서드 (이름 변경됨)
        __ 더블 언더스코어로 시작
        외부에서 직접 접근 어려움
        """
        return "private"
    
    def access_private(self):
        """내부에서만 접근 가능"""
        return self.__private_method()

# 사용 예시
obj = MyClass()
obj.public_method()  # ✅ 가능
obj._protected_method()  # ⚠️ 가능하지만 권장하지 않음
obj.__private_method()  # ❌ AttributeError
obj.access_private()  # ✅ 내부 메서드로 접근
```

## 6. 주의사항

### 생성자 리턴값

```python
class MyClass:
    def __init__(self):
        # ❌ 생성자에서 명시적인 값 반환 불가
        # return "something"  # TypeError 발생
        
        # ✅ None만 반환 가능 (생략 가능)
        return None  # 또는 return 생략
```

### 클래스 변수와 인스턴스 변수 구분

```python
class Example:
    shared = []  # 클래스 변수 (모든 인스턴스가 공유)
    
    def __init__(self):
        self.unique = []  # 인스턴스 변수 (각 인스턴스마다 독립적)

# 주의: 클래스 변수는 모든 인스턴스가 공유
obj1 = Example()
obj2 = Example()
obj1.shared.append(1)
obj2.shared.append(2)
print(obj1.shared)  # [1, 2]
print(obj2.shared)  # [1, 2] (같은 리스트 공유)

# 인스턴스 변수는 독립적
obj1.unique.append(1)
obj2.unique.append(2)
print(obj1.unique)  # [1]
print(obj2.unique)  # [2]
```

---

**작성일**: 2024  
**참고**: Python 3.x 기준

