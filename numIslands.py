class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dirs = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        def inbound(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return False

            return True

        def dfs(i, j):
            grid[i][j] = "0"
            for dir in dirs:
                if inbound(i + dir[0], j+ dir[1]):
                    dfs(i + dir[0], j+ dir[1])


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count




