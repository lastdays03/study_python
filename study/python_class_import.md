# 파이썬 클래스 Import 문법 가이드

## 1. 기본 Import 문법

### 같은 디렉토리에서 클래스 import

```python
# test.py 파일에서 Test 클래스를 다른 파일로 import
from test import Test

# 또는
import test
obj = test.Test()
```

### 다른 디렉토리에서 클래스 import

```python
# 패키지 구조가 다음과 같을 때:
# project/
#   ├── utils/
#   │   └── helpers.py  (MyClass 정의)
#   └── main.py

# main.py에서:
from utils.helpers import MyClass
# 또는
from utils import helpers
obj = helpers.MyClass()
```

## 2. 다양한 Import 방법

### 개별 클래스 import

```python
from module import ClassName
obj = ClassName()
```

### 여러 클래스 한 번에 import

```python
from module import Class1, Class2, Class3
obj1 = Class1()
obj2 = Class2()
```

### 모듈 전체 import

```python
import module
obj = module.ClassName()
```

### 별칭(alias) 사용

```python
from module import ClassName as CN
obj = CN()

# 또는 모듈에 별칭
import module as mod
obj = mod.ClassName()
```

### 모든 클래스 import (권장하지 않음)

```python
from module import *  # 모든 공개 클래스/함수 import
obj = ClassName()  # module. 없이 직접 사용 가능
```

## 3. 패키지 구조 예시

```
project/
├── __init__.py
├── models/
│   ├── __init__.py
│   └── user.py      # User 클래스
└── main.py
```

```python
# models/__init__.py에서
from .user import User  # 상대 경로 import

# main.py에서
from models import User
# 또는
from models.user import User
```

## 4. 실제 사용 예시

### test.py 파일의 Test 클래스 사용

```python
# 다른 파일에서 test.py의 Test 클래스 사용
from test import Test

# 인스턴스 생성
test_obj = Test("홍길동", 25)
```

## 5. 주의사항

- ✅ `__init__.py` 파일이 있어야 패키지로 인식됩니다 (Python 3.3+에서는 선택적)
- ❌ 순환 import를 피하세요
- ⚠️ `from module import *`는 가독성을 저하시킬 수 있으므로 지양하세요
- 📁 상대 경로 import는 `.` (현재 디렉토리) 또는 `..` (상위 디렉토리)를 사용합니다

## 6. 상대 경로 Import

```python
# 같은 패키지 내에서
from .module import ClassName      # 현재 디렉토리
from ..module import ClassName     # 상위 디렉토리
from ...module import ClassName    # 상위의 상위 디렉토리
```

## 7. 조건부 Import

```python
try:
    from module import ClassName
except ImportError:
    # 대체 처리
    ClassName = None
```

## 8. 타입 힌팅과 함께 사용

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module import ClassName

def function(param: 'ClassName') -> None:
    pass
```

---

**작성일**: 2024
**참고**: Python 3.x 기준

