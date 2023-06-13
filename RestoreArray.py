n = int(input())
for test in range(n):
    lenght = int(input())
    arr = list(map(int, input().split()))
    res = [0] * lenght
    
    res[0] = arr[0]
    res[-1] = arr[-1]
    
    for i in range(lenght - 2):
        res[i+1] = min(arr[i], arr[i+1])
        
    print(*res)
    
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
