
def two_power_arr(x):
    cur = 1
    while cur <= x:
        cur *= 2
    return cur
 
t = int(input())
for _ in range(t):
    n = int(input())
    lists = list(map(int, input().split()))
    
    print(n)
    for i in range(1, n +1):
        print(i, two_power_arr(lists[i - 1]) -lists[i - 1])
        
    """
    Time Complexity: O(logn) 
    Space Complexity: O(1)
    """
