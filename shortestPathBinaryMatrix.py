class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        visited = set()
        start = (0,0,1)
        queue = deque([start])

        n = len(grid)

        def inbound(new_row, new_col):
            if (0 <= new_row < len(grid)) and (0  <= new_col < len(grid[0])) and grid[new_row][new_col] == 0:
                return True

        while queue:
            r, c, length = queue.popleft()
            
            if r == c == (n-1):
                return length
            for row, col in dirs:
                new_row = r + row
                new_col = c + col
           
                if inbound(new_row, new_col) and (new_row, new_col) not in visited: 
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, length + 1))
        
        return -1
