class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        start = word[0]
        matchCount = len(word)

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def choose(r, c, idx):
            if (idx == matchCount):
                return True

            if (r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]):
                return False

            temp = board[r][c]
            board[r][c] = "#"
            
            for d in range(4):
                if (choose(r + dr[d], c + dc[d], idx + 1)):
                    board[r][c] = "#"
                    return True

            board[r][c] = temp
            return False

            
        for i in range(m):
            for j in range(n):
                if (board[i][j] == start):
                    if choose(i, j, 0):
                            return True
                
        return False