class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_len = len(board)
        col_len = len(board[0])

        def dfs(visited, loc):
            visited.add(loc)
            i, j = loc
            if i == 0 or i == row_len - 1:
                return False
            if j == 0 or j == col_len - 1:
                return False
            
            state = True
            if board[i-1][j] == "O" and (i-1, j) not in visited:
                state = state and dfs(visited, (i-1, j))
            if board[i+1][j] == "O" and (i+1, j) not in visited:
                state = state and dfs(visited, (i+1, j))
            if board[i][j-1] == "O" and (i, j-1) not in visited:
                state = state and dfs(visited, (i, j-1))
            if board[i][j+1] == "O" and (i, j+1) not in visited:
                state = state and dfs(visited, (i, j+1))

            return state

        for row in range(row_len):
            for col in range(col_len):
                visited = set()
                if board[row][col] == "O" and dfs(visited, (row, col)):
                    for i, j in visited:
                        board[i][j] = "X"

        return board