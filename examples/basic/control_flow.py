#!/usr/bin/env python3
"""
기본 예제: 제어 구조
Basic Example: Control Flow

조건문과 반복문의 사용법을 보여줍니다.
Demonstrates the use of conditionals and loops.
"""

def conditional_example():
    """조건문 예제 (Conditional Example)"""
    print("=== 조건문 예제 (Conditional Example) ===")
    
    score = 85
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"점수: {score}, 학점: {grade}")

def loop_example():
    """반복문 예제 (Loop Example)"""
    print("\n=== 반복문 예제 (Loop Example) ===")
    
    # for 반복문
    print("for 문 - 1부터 5까지:")
    for i in range(1, 6):
        print(f"  {i}")
    
    # while 반복문
    print("\nwhile 문 - 카운트다운:")
    count = 5
    while count > 0:
        print(f"  {count}...")
        count -= 1
    print("  발사!")

def nested_loop_example():
    """중첩 반복문 예제 (Nested Loop Example)"""
    print("\n=== 구구단 2단 (Multiplication Table 2) ===")
    
    dan = 2
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} x {i} = {result}")

def main():
    conditional_example()
    loop_example()
    nested_loop_example()

if __name__ == "__main__":
    main()
