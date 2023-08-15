t= int(input())
for _ in range(t):
    matrix = []
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    for val in row1:
        matrix.append(val)
    for val in row2:
        matrix.append(val)
    
    high = matrix.index(max(matrix))
    low = matrix.index(min(matrix))
    if high + low == 3:
        print("YES")
    else:
        print("NO")
