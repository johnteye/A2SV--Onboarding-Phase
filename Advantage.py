t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_b = sorted(arr)
    res = []
    for i in range(n):
        if arr[i] == arr_b[n - 1]:
            res.append(arr[i] - arr_b[n - 2])
            
        else:
            res.append(arr[i] - arr_b[n - 1])
            
            
    print(*res)
