#!/usr/bin/env python3
"""
기본 예제: 변수와 데이터 타입
Basic Example: Variables and Data Types

다양한 데이터 타입과 변수 사용법을 보여줍니다.
Demonstrates various data types and variable usage.
"""

def main():
    # 정수형 (Integer)
    age = 25
    print(f"나이 (Age): {age}")
    
    # 실수형 (Float)
    height = 175.5
    print(f"키 (Height): {height}cm")
    
    # 문자열 (String)
    name = "김학생"
    print(f"이름 (Name): {name}")
    
    # 불린 (Boolean)
    is_student = True
    print(f"학생 여부 (Is Student): {is_student}")
    
    # 리스트 (List)
    scores = [90, 85, 88, 92, 87]
    print(f"점수 목록 (Scores): {scores}")
    print(f"평균 점수 (Average): {sum(scores) / len(scores):.2f}")
    
    # 딕셔너리 (Dictionary)
    student = {
        "name": "이학생",
        "age": 22,
        "major": "Computer Science"
    }
    print(f"학생 정보 (Student Info): {student}")

if __name__ == "__main__":
    main()
