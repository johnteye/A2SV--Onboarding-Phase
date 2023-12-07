class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        def inbound(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return False

            return True

        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            for dir in dirs:
                if inbound(i + dir[0], j+ dir[1]):
                    area += dfs(i + dir[0], j+ dir[1])
            return area


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        
        return res
