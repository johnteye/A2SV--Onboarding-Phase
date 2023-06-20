class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        transposed = [ [0]* rows for _ in range(cols)]

        for col_idx in range(len(matrix[0])):
            for row_idx in range(len(matrix)):
                transposed[col_idx][row_idx] = matrix[row_idx][col_idx]
        
        return transposed

        """
        Time Complexity: O(N^**2)
        Space Complexity: O(N)
        """
