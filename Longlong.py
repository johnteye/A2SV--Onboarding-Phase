t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
                    
    # -1 7 -4 -2 5 -8
    flag = False
    count = 0
    total = 0
    for i in range(n):
        total += abs(arr[i])
        
        if arr[i] < 0 and not flag:
            count += 1
            flag = True 
            
        elif arr[i] > 0:
            flag = False
        
    print(total, count)
