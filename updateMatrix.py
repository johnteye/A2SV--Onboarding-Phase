class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        queue = deque()

        def inbound(new_row, new_col):
            if 0 <= new_row < len(mat) and  0 <= new_col < len(mat[0]):
                return True

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col, 0))
        
        while queue:
            r, c , step = queue.popleft()

            for dr, dc in dirs:
                new_row = r + dr
                new_col = c + dc

                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    if mat[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, step + 1))

                        mat[new_row][new_col] = step + 1

                
        return mat

