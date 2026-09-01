# [재귀 함수 - 팩토리얼과 피보나치 수열]
# RECURSION TAIL 방식 풀이


def facto_tail(n, acc = 1):
    if (n == 0):
        return acc
    
    return facto_tail(n - 1, acc * n)


def fibo_tail(n, prev = 1, prevprev = 0):
    if (n == 0):
        return 0
    
    elif (n != 0 and n <= 2):
        return prev

    return fibo_tail(n - 1, prev + prevprev, prev)


# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = facto_tail(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibo_tail(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {facto_tail(10)}")
    print(f"fib(15) = {fibo_tail(15)}")