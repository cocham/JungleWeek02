# 리스트 컴프리헨션 풀이

def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수
    
    Args:
        students: 학생 정보 딕셔너리 리스트
    
    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """

    scores = [student["score"] for student in students]
    avg = sum(scores) / len(scores)
    above_avg_students = [student["name"] for student in students if student["score"] >= avg]
    
    return avg, above_avg_students



# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")