from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    result += [(i, element), (element, j), (i // 3, j // 3, element)]

        return len(result) == len(set(result))
    
print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))