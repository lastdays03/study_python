# 파이썬 클래스 고급 기능

## 1. 특수 메서드 (Magic Methods)

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """문자열 표현 (사용자 친화적) - str() 함수 사용 시 호출"""
        return f"{self.name} ({self.age}세)"
    
    def __repr__(self) -> str:
        """객체 표현 (개발자용, 디버깅) - repr() 함수 사용 시 호출"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __len__(self) -> int:
        """len() 함수 사용 시 호출"""
        return self.age
    
    def __eq__(self, other: object) -> bool:
        """== 연산자 사용 시 호출"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age
    
    def __add__(self, other: 'Person') -> 'Person':
        """+ 연산자 사용 시 호출"""
        return Person(f"{self.name}+{other.name}", self.age + other.age)
    
    def __lt__(self, other: 'Person') -> bool:
        """< 연산자 사용 시 호출"""
        return self.age < other.age

# 사용 예시
p1 = Person("홍길동", 25)
p2 = Person("김철수", 30)

print(str(p1))  # 홍길동 (25세)
print(repr(p1))  # Person(name='홍길동', age=25)
print(len(p1))  # 25
print(p1 == p2)  # False
print(p1 < p2)  # True
p3 = p1 + p2
print(p3)  # 홍길동+김철수 (55세)
```

### 주요 특수 메서드 목록

| 메서드 | 설명 | 예시 |
|--------|------|------|
| `__init__` | 생성자 | 객체 생성 시 호출 |
| `__str__` | 문자열 표현 | `str(obj)` |
| `__repr__` | 객체 표현 | `repr(obj)` |
| `__len__` | 길이 | `len(obj)` |
| `__eq__` | 같음 비교 | `obj1 == obj2` |
| `__ne__` | 다름 비교 | `obj1 != obj2` |
| `__lt__` | 작음 비교 | `obj1 < obj2` |
| `__le__` | 작거나 같음 | `obj1 <= obj2` |
| `__gt__` | 큼 비교 | `obj1 > obj2` |
| `__ge__` | 크거나 같음 | `obj1 >= obj2` |
| `__add__` | 덧셈 | `obj1 + obj2` |
| `__sub__` | 뺄셈 | `obj1 - obj2` |
| `__getitem__` | 인덱싱 | `obj[key]` |
| `__setitem__` | 인덱싱 할당 | `obj[key] = value` |

## 2. 프로퍼티 (Property) - getter/setter

```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """getter - 값을 읽을 때 호출"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """setter - 값을 설정할 때 호출"""
        if value < -273.15:
            raise ValueError("절대 영도보다 낮을 수 없습니다")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """읽기 전용 프로퍼티 (setter 없음)"""
        return self._celsius * 9/5 + 32

# 사용 예시
temp = Temperature(25)
print(temp.celsius)  # 25 (getter 호출)
print(temp.fahrenheit)  # 77.0 (getter 호출)
temp.celsius = 30  # setter 호출
# temp.fahrenheit = 100  # ❌ AttributeError (setter 없음)
```

### 프로퍼티를 사용하는 이유

```python
# ❌ 나쁜 예: 직접 접근
class Person:
    def __init__(self, age: int):
        self.age = age  # 음수 값도 들어올 수 있음

# ✅ 좋은 예: 프로퍼티 사용
class Person:
    def __init__(self, age: int):
        self._age = age
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("나이는 0 이상이어야 합니다")
        self._age = value
```

## 3. 추상 메서드 (Abstract Method)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """추상 클래스 - 직접 인스턴스화 불가"""
    
    @abstractmethod
    def make_sound(self) -> str:
        """추상 메서드 (하위 클래스에서 반드시 구현)"""
        pass
    
    @abstractmethod
    def move(self) -> None:
        """추상 메서드"""
        pass
    
    def sleep(self) -> None:
        """일반 메서드 (구현 가능)"""
        print("잠을 잡니다")

class Dog(Animal):
    def make_sound(self) -> str:
        """추상 메서드 구현"""
        return "멍멍"
    
    def move(self) -> None:
        """추상 메서드 구현"""
        print("네 발로 걷기")

class Cat(Animal):
    def make_sound(self) -> str:
        """추상 메서드 구현"""
        return "야옹"
    
    def move(self) -> None:
        """추상 메서드 구현"""
        print("네 발로 걷기")

# animal = Animal()  # ❌ 오류 (추상 클래스는 인스턴스화 불가)
dog = Dog()  # ✅ 가능
cat = Cat()  # ✅ 가능

print(dog.make_sound())  # 멍멍
cat.move()  # 네 발로 걷기
```

## 4. 실제 사용 예시

```python
from typing import Optional, List
from datetime import datetime
from abc import ABC, abstractmethod

class BankAccount:
    """은행 계좌 클래스"""
    
    account_count = 0
    interest_rate = 0.02
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        BankAccount.account_count += 1
        self.account_number = BankAccount.account_count
        self.owner = owner
        self._balance = initial_balance
        self.transaction_history: List[str] = []
    
    @property
    def balance(self) -> float:
        """잔액 조회 (읽기 전용)"""
        return self._balance
    
    def deposit(self, amount: float) -> float:
        """입금"""
        if amount <= 0:
            raise ValueError("입금 금액은 0보다 커야 합니다")
        self._balance += amount
        self.transaction_history.append(
            f"{datetime.now()}: 입금 {amount:,.0f}원"
        )
        return self._balance
    
    def withdraw(self, amount: float) -> float:
        """출금"""
        if amount <= 0:
            raise ValueError("출금 금액은 0보다 커야 합니다")
        if amount > self._balance:
            raise ValueError("잔액이 부족합니다")
        self._balance -= amount
        self.transaction_history.append(
            f"{datetime.now()}: 출금 {amount:,.0f}원"
        )
        return self._balance
    
    def __str__(self) -> str:
        """문자열 표현"""
        return f"{self.owner}님의 계좌 (잔액: {self._balance:,.0f}원)"
    
    def __repr__(self) -> str:
        """객체 표현"""
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"
    
    def __eq__(self, other: object) -> bool:
        """같은 계좌인지 비교"""
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.account_number == other.account_number
    
    def __lt__(self, other: 'BankAccount') -> bool:
        """잔액 비교"""
        return self._balance < other._balance
    
    @classmethod
    def get_account_count(cls) -> int:
        """총 계좌 수 조회"""
        return cls.account_count
    
    @staticmethod
    def calculate_interest(principal: float, years: int) -> float:
        """이자 계산"""
        return principal * BankAccount.interest_rate * years

# 사용 예시
account1 = BankAccount("홍길동", 10000)
account2 = BankAccount("김철수", 5000)

print(account1)  # 홍길동님의 계좌 (잔액: 10,000원)
print(account1.balance)  # 10000.0 (프로퍼티)
print(account1 == account2)  # False
print(account1 < account2)  # False (10000 < 5000)
print(BankAccount.calculate_interest(10000, 1))  # 200.0
```

---

**작성일**: 2024  
**참고**: Python 3.x 기준

