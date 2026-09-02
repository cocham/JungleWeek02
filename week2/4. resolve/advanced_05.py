# N-QUEEN
# NXN 체스판에서 상하좌우대각선 8방향에 안 걸리는 경우의 수 찾기
# 퀸을 배치 시킬 때마다 해당 열에서 안전한지 검사해야함


def n_queens(n: int) -> int:
    cols = [0] * n
    count = 0
    
    def put(c):
        nonlocal count
        
        if (c == n):
            count += 1
            return
        
        for r in range(n):
            if (isSafe(r, c)):
                cols[c] = r
                put(c + 1)
                
    def isSafe(r, c):
        for i in range(c):
            if (cols[i] == r):
                return False
            if (abs(cols[i] - r) == abs(i - c)):
                return False
            
        return True
    
    put(0)
    return count
    

if __name__ == "__main__":
    print("[테스트] N=1 ~ N=8 에 대한 가능한 배치의 수")
    for n in range(1, 9):
        print(f"  N={n}: {n_queens(n)}")

