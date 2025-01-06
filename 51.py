class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["."] * n for _ in range(n)]
        
        res = []
        
        visited_cols = set()
        visited_diagonals = set()
        visited_antidiagonals = set()
        
        def backtracking(row):
            if row == n:
                res.append(["".join(row_info) for row_info in board])
                
            for col in range(n):
                diff = row - col
                sum = row + col
                
                if not (col in visited_cols or diff in visited_diagonals or sum in visited_antidiagonals):
                    visited_cols.add(col)
                    visited_diagonals.add(diff)
                    visited_antidiagonals.add(sum)
                    board[row][col] = "Q"
                    backtracking(row + 1)
                    
                    visited_cols.remove(col)
                    visited_diagonals.remove(diff)
                    visited_antidiagonals.remove(sum)
                    board[row][col] = "."
                
        backtracking(0)
        return res

sol = Solution().solveNQueens(4)
print(sol)