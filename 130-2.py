class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_len = len(board)
        col_len = len(board[0])
        res = [["X"] * col_len for row in range(row_len)]

        def dfs(visited, loc):
            visited.add(loc)
            i, j = loc
            res[i][j] = "O"
            
            if i > 0 and board[i-1][j] == "O" and (i-1, j) not in visited:
                dfs(visited, (i-1, j))
            if i < row_len - 1 and board[i+1][j] == "O" and (i+1, j) not in visited:
                dfs(visited, (i+1, j))
            if j > 0 and board[i][j-1] == "O" and (i, j-1) not in visited:
                dfs(visited, (i, j-1))
            if j < col_len - 1 and board[i][j+1] == "O" and (i, j+1) not in visited:
                dfs(visited, (i, j+1))

        visited = set()
        for col in range(col_len):
            if board[0][col] == "O" and (0, col) not in visited:
                dfs(visited, (0, col))
            if board[row_len-1][col] == "O" and (row_len-1, col) not in visited:
                dfs(visited, (row_len-1, col))

        for row in range(row_len):
            if board[row][0] == "O" and (row, 0) not in visited:
                dfs(visited, (row, 0))
            if board[row][col_len-1] == "O" and (row, col_len-1) not in visited:
                dfs(visited, (row, col_len-1))

        for row in range(row_len):
            for col in range(col_len):
                board[row][col] = res[row][col]
        return board