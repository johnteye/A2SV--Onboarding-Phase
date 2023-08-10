
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        if (arr[i] - i - 1) % k != 0:
            count += 1
            
    if count == 0:
        print(0)
    elif count <=2:
        print(1)
        
    else:
        print(-1)
        

"""
time complexity: O(n)
space complexity: O(1)
"""
