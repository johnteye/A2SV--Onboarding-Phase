class Solution:
    def isMagicSquare(self, matrix):

        res = 0
        # rowcount
        row_sum = 0
        col_sum = 0
        mdiag_sum = 0
        sdiag_sum = 0
        row_count = []
        col_count = []
        row_check = False
        col_check = False
        mdiag_check = False
        sdiag_check = False

        for row_idx in range(3):
            row_sum = 0
            for col_idx in range(3):
                row_sum += matrix[row_idx][col_idx]
                if row_idx == col_idx:
                    mdiag_sum += matrix[row_idx][col_idx]
                if row_idx + col_idx == 2:
                    sdiag_sum += matrix[row_idx][col_idx]
            row_count.append(row_sum)
        for col_idx in range(3):
            col_sum = 0
            for row_idx in range(3):
                col_sum += matrix[row_idx][col_idx]
            col_count.append(col_sum)


        if len(set(row_count)) == 1 or len(set(col_count)) ==  1:
            row_check = True
            col_check = True
        else:
            row_check = False
            col_check = False

        if row_check and col_check and mdiag_sum == row_count[0]:
            mdiag_check = True
        else:
            mdiag_check = False

        if row_check and col_check and sdiag_sum == row_count[0]:
            sdiag_check = True
        else:
            sdiag_check = False

        if row_sum == col_sum == mdiag_sum == sdiag_sum:
            res += 1
            return res
        else: 
            return res
    def isdistinct(self, matrix):
        elements = [element for row in matrix for element in row]
        for i in range(len(elements)):
            for j in range(i + 1, len(elements)):
                if elements[i] == elements[j]:
                    return False
        
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        sub_matrices = []
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sub_matrix = []
                sub_matrix.append(grid[i][j:j+3])
                sub_matrix.append(grid[i+1][j:j+3])
                sub_matrix.append(grid[i+2][j:j+3])
                sub_matrices.append(sub_matrix)
        ans = 0
        
        for mat in sub_matrices:
            max_val = max(max(row) for row in mat)
            min_val = min(min(row) for row in mat)

            if self.isdistinct(mat) and max_val <=9 and min_val >= 1:
                ans += self.isMagicSquare(mat)

        return ans

    

            

