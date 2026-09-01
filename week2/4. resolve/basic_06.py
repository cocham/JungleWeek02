"""
[백트래킹]
    1 부터 n 까지 숫자 중 k 개를 선택하는 모든 조합을 반환합니다.

    Args:
    n: 전체 숫자 개수 (1, 2, ..., n)
    k: 선택할 개수

    Returns:
    모든 조합을 담은 리스트(예: [[1,2], [1,3], ...])
"""


def combinations(n: int, k: int) -> list:

    result = []
    current = []    
    
    def choose(start):
        if (len(current) == k):
            result.append(current[:])
            return
        
        for i in range(start, n + 1):
            current.append(i)
            choose(i + 1)
            current.pop()
        
    choose(1)
    return result



# ============================================================================
# 테스트 케이스
# ============================================================================
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()

    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()

    # 테스트 케이스 3
    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()

    # 테스트 케이스 4
    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")