dimensions = list(map(int, input().split()))
row, col = dimensions[0], dimensions[1]

matrix =[]
output = []

for _ in range(0, row):
    matrix.append(list(input()))

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[0])):
        curr_row = matrix[row_idx]
        curr_col = [matrix[x][col_idx] for x in range(0, row)]
        
        if curr_row.count(matrix[row_idx][col_idx]) == 1 and curr_col.count(matrix[row_idx][col_idx]) == 1:
            
            output.append(matrix[row_idx][col_idx])
            
          
print(''.join(output))

"""
Time complexity: O(n2)
Space complexity: O(1)
"""
