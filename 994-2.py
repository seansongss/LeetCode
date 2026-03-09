class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len, col_len = len(grid), len(grid[0])
        q = []
        fresh = 0

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_t, rotten = 0, 0

        while q:
            r, c, t = q.pop(0)
            max_t = max(max_t, t)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
                    rotten += 1
        
        return max_t if rotten == fresh else -1