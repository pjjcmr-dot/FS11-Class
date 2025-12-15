#!/usr/bin/env python3
"""
심화 예제: 함수
Advanced Example: Functions

함수의 정의와 사용법을 보여줍니다.
Demonstrates function definition and usage.
"""

def greet(name):
    """간단한 인사 함수 (Simple greeting function)"""
    return f"안녕하세요, {name}님!"

def calculate_average(numbers):
    """평균 계산 함수 (Average calculation function)"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def factorial(n):
    """재귀 함수 예제: 팩토리얼 (Recursive function: Factorial)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def process_student_data(name, age, *subjects, **info):
    """가변 인자 예제 (Variable arguments example)"""
    print(f"이름: {name}, 나이: {age}")
    print(f"수강 과목: {', '.join(subjects)}")
    print(f"추가 정보: {info}")

def main():
    # 기본 함수 호출
    print(greet("홍길동"))
    
    # 리스트를 인자로 전달
    scores = [85, 90, 78, 92, 88]
    avg = calculate_average(scores)
    print(f"평균 점수: {avg:.2f}")
    
    # 재귀 함수
    print(f"5! = {factorial(5)}")
    
    # 가변 인자
    process_student_data(
        "김학생", 
        22, 
        "수학", "영어", "과학",
        major="컴퓨터공학",
        semester=3
    )

if __name__ == "__main__":
    main()
