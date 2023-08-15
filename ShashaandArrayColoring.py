
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    # check how many colors
    
    colors =  n // 2 
    # 1 3 4 5 6 
    #   i   j
    # cost = 6 - 1= 2
    # total = 7
    
    
    total = 0
    j = len(arr) -1
    
    for i in range(colors):
        cost = arr[j] - arr[i]
        total += cost
        
        j -= 1
        
    print(total)
  
        
        
