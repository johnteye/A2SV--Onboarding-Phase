t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    i, j = 0, len(arr) -1
 
    
    while i < j:
        res.append(arr[i])
        res.append(arr[j])
        
        i += 1
        j -= 1
        if i == j:
            res.append(arr[i])
    if len(arr) == 1:
        print(*arr)
    else:
        print(*res)
