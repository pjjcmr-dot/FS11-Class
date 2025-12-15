# 코딩 표준 (Coding Standards)

## 일반 원칙 (General Principles)

### 1. 가독성 (Readability)
- 명확하고 이해하기 쉬운 코드 작성
- 의미 있는 변수명과 함수명 사용
- 적절한 들여쓰기와 공백 사용

### 2. 일관성 (Consistency)
- 프로젝트 전체에서 동일한 스타일 유지
- 팀의 코딩 규칙 따르기
- 스타일 가이드 준수

### 3. 간결성 (Simplicity)
- 불필요한 복잡성 피하기
- KISS 원칙 (Keep It Simple, Stupid)
- DRY 원칙 (Don't Repeat Yourself)

## 네이밍 규칙 (Naming Conventions)

### Python
```python
# 변수와 함수: snake_case
user_name = "홍길동"
def calculate_average(numbers):
    pass

# 클래스: PascalCase
class StudentManager:
    pass

# 상수: UPPER_CASE
MAX_STUDENTS = 100
```

### JavaScript
```javascript
// 변수와 함수: camelCase
let userName = "홍길동";
function calculateAverage(numbers) {
    // ...
}

// 클래스: PascalCase
class StudentManager {
    // ...
}

// 상수: UPPER_CASE
const MAX_STUDENTS = 100;
```

## 주석 작성 (Comments)

### 좋은 주석
```python
# 사용자 입력 유효성 검사
def validate_input(data):
    """
    입력 데이터의 유효성을 검사합니다.
    
    Args:
        data (dict): 검사할 데이터
        
    Returns:
        bool: 유효하면 True, 아니면 False
    """
    return data is not None and len(data) > 0
```

### 피해야 할 주석
```python
# 나쁜 예: 코드를 그대로 설명
i = i + 1  # i에 1을 더함

# 좋은 예: 의도를 설명
i = i + 1  # 다음 페이지로 이동
```

## 코드 구조 (Code Structure)

### 함수 크기
- 한 함수는 한 가지 일만 수행
- 함수는 가능한 짧게 (20-30줄 이내 권장)
- 복잡한 로직은 여러 함수로 분리

### 들여쓰기
```python
# 4칸 들여쓰기 사용
def example_function():
    if condition:
        do_something()
    else:
        do_something_else()
```

## 에러 처리 (Error Handling)

### 적절한 예외 처리
```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return None
    except TypeError:
        print("숫자만 입력하세요.")
        return None
    else:
        return result
```

## 테스트 (Testing)

### 단위 테스트 작성
```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
```

## 버전 관리 (Version Control)

### 커밋 메시지 규칙
```
타입: 제목

본문 (선택사항)

꼬리말 (선택사항)
```

예시:
```
feat: 사용자 로그인 기능 추가

로그인 폼과 인증 로직을 구현했습니다.
- JWT 토큰 기반 인증
- 비밀번호 암호화

Closes #123
```

### 커밋 타입
- `feat`: 새로운 기능
- `fix`: 버그 수정
- `docs`: 문서 수정
- `style`: 코드 포맷팅
- `refactor`: 코드 리팩토링
- `test`: 테스트 추가/수정
- `chore`: 기타 변경사항

## 코드 리뷰 체크리스트 (Code Review Checklist)

- [ ] 코드가 요구사항을 충족하는가?
- [ ] 변수명과 함수명이 명확한가?
- [ ] 주석이 적절하게 작성되었는가?
- [ ] 에러 처리가 되어있는가?
- [ ] 테스트 케이스가 있는가?
- [ ] 코드 중복이 없는가?
- [ ] 성능상 문제가 없는가?
- [ ] 보안 취약점이 없는가?
