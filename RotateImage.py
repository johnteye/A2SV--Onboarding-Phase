class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0]) 

        data = []
        for col_idx in range(col):
            array = []
            for row_idx in range(row-1, -1, -1):
                array.append(matrix[row_idx][col_idx])
            data.append(array)
        for i in range(len(data)):
            matrix[i]=data[i]
        return matrix


"""
Time Complexity: O(N2)
Space complexity: O(1)
"""
