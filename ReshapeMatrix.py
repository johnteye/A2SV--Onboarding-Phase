class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if row * col  != r * c: return mat

        new_mat = []
        curr_row = []
        for i in range(row):
            for j in range(col):
                curr_row.append(mat[i][j])
                if len(curr_row) == c:
                    new_mat.append(curr_row)
                    curr_row = []

        return new_mat
            
"""
Time Complexity: O(N **2)
Space Complexity: O(1)
"""
