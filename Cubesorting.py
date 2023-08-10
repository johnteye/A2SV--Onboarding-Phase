t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    inc = False
    
    for i in range(1, n):
        if arr[i-1] <= arr[i]:
            inc = True
            
    if inc:
        print("YES")
        
    else:
        print("NO")

"""
time complexity: O(n)
space complexity:O(1)
"""
