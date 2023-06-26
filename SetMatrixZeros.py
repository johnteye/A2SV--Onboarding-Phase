class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == [] or matrix == [[]]:
            return matrix
        
        ZeroRows = set()
        ZeroCols = set()
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ZeroRows.add(i)
                    ZeroCols.add(j)
                    
        for row_idx in range(row):
            for col_idx in ZeroCols:
                matrix[row_idx][col_idx] = 0
                
        for col_idx in range(col):
            for row_idx in ZeroRows:
                matrix[row_idx][col_idx] = 0

        return matrix


"""
Time Complexity: O(N**2)
Space Complexity: O(1)
"""
