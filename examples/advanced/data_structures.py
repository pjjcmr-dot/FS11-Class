#!/usr/bin/env python3
"""
심화 예제: 데이터 구조
Advanced Example: Data Structures

다양한 데이터 구조의 사용법을 보여줍니다.
Demonstrates the use of various data structures.
"""

def list_operations():
    """리스트 연산 (List operations)"""
    print("=== 리스트 (List) ===")
    
    fruits = ["사과", "바나나", "오렌지"]
    print(f"초기 리스트: {fruits}")
    
    # 요소 추가
    fruits.append("포도")
    print(f"추가 후: {fruits}")
    
    # 요소 제거
    fruits.remove("바나나")
    print(f"제거 후: {fruits}")
    
    # 리스트 컴프리헨션
    numbers = [i ** 2 for i in range(1, 6)]
    print(f"제곱수: {numbers}")

def dictionary_operations():
    """딕셔너리 연산 (Dictionary operations)"""
    print("\n=== 딕셔너리 (Dictionary) ===")
    
    student = {
        "name": "이학생",
        "age": 22,
        "major": "Computer Science"
    }
    
    print(f"학생 정보: {student}")
    print(f"이름: {student['name']}")
    
    # 키-값 쌍 추가
    student["grade"] = "A"
    print(f"성적 추가 후: {student}")
    
    # 딕셔너리 순회
    print("모든 정보:")
    for key, value in student.items():
        print(f"  {key}: {value}")

def set_operations():
    """세트 연산 (Set operations)"""
    print("\n=== 세트 (Set) ===")
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"합집합: {set1 | set2}")
    print(f"교집합: {set1 & set2}")
    print(f"차집합: {set1 - set2}")

def tuple_operations():
    """튜플 연산 (Tuple operations)"""
    print("\n=== 튜플 (Tuple) ===")
    
    coordinates = (10, 20)
    print(f"좌표: {coordinates}")
    print(f"X: {coordinates[0]}, Y: {coordinates[1]}")
    
    # 튜플 언패킹
    x, y = coordinates
    print(f"언패킹: x={x}, y={y}")

def main():
    list_operations()
    dictionary_operations()
    set_operations()
    tuple_operations()

if __name__ == "__main__":
    main()
