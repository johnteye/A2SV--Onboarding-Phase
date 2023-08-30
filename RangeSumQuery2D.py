class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.prefix_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                if row_idx == 0:
                    self.prefix_matrix[row_idx][col_idx] = self.prefix_matrix[row_idx][col_idx-1] + matrix[row_idx][col_idx]

                elif col_idx == 0:
                    self.prefix_matrix[row_idx][col_idx] = self.prefix_matrix[row_idx-1][col_idx] + matrix[row_idx][col_idx]

                else:
                    self.prefix_matrix[row_idx][col_idx] = self.prefix_matrix[row_idx][col_idx-1] + self.prefix_matrix[row_idx - 1][col_idx] + matrix[row_idx][col_idx] - self.prefix_matrix[row_idx-1][col_idx -1]

                



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1== col1==0:
            return self.prefix_matrix[row2][col2]
        elif col1 == 0:
            res = self.prefix_matrix[row2][col2] - self.prefix_matrix[row1-1][col2]
        elif row1 ==0:
            res = self.prefix_matrix[row2][col2] - self.prefix_matrix[row2][col1-1]
        else:
            res = self.prefix_matrix[row2][col2]- self.prefix_matrix[row2][col1-1] - self.prefix_matrix[row1-1][col2] + self.prefix_matrix[row1-1][col1-1]

        return res

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
