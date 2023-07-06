t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    matrix = []
    for i in range(n):
        row = list(map(str,input()))
        matrix.append(row)
        
    def move_down(matrix, r, c):
        cur_row = r
        for next_row in range(r + 1, n):
            if matrix[next_row][c] == ".":
                matrix[next_row][c], matrix[cur_row][c] = matrix[cur_row][c], matrix[next_row][c]
                cur_row = next_row
            else:
                break
            
            
    for c in range(m):
        for r in range(n-1, -1, -1):
            cell = matrix[r][c]
            if cell == ".":
                continue
            elif cell == "o":
                continue
            else:
                move_down(matrix, r, c)
        
    for res in matrix:
        print("".join(res))
        
    print()
    
"""
Time complexity: O(N*M)
Space complexity: O(N*M)
  """
