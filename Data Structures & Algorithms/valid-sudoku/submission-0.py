class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map1, map2, map3 = [[0] * 10 for _ in range(9)], [[0] * 10 for _ in range(9)], [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                col = ord(board[i][j]) - ord('1')
                row = ord(board[j][i]) - ord('1')
                if board[i][j] != '.':
                    map1[i][col] += 1
                    if map1[i][col] > 1: return False
                if board[j][i] != '.':
                    map2[i][row] += 1
                    if map2[i][row] > 1: return False
                if board[i][j] != '.':
                    map3[(i//3) * 3 + (j//3)][col] += 1
        if any(map3[i][j] > 1 for i in range(9) for j in range(10)) : return False
        return True

        