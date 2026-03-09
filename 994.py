class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        org_dict = {0: [], 1: [], 2: []}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                org_dict[grid[row][col]].append((row, col))
        
        
        def bfs(pos):
            if pos in visited:
                return
            
            row, col = pos
            adj = []
            if row > 0:
                adj.append((row-1, col))
            if row < len(grid) - 1:
                adj.append((row+1, col))
            if col > 0:
                adj.append((row, col-1))
            if col < len(grid[0]) - 1:
                adj.append((row, col+1))

            print(adj)
            for loc in adj:
                i, j = loc
                if grid[i][j] == 1 and (i, j) in org_dict[1]:
                    org_dict[1].remove((i, j))
                    org_dict[2].append((i,j))
                    queue.append((i,j))

        queue = org_dict[2]
        visited = set()
        cnt = -1

        while queue:
            queue_len = len(queue)
            print(queue_len)
            print(queue)
            for _ in range(queue_len):
                bfs(queue.pop(0))
                visited.add(pos)

            cnt += 1

        if org_dict[1]:
            return -1

        if cnt == -1:
            return 0

        return cnt