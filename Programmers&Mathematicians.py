t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    left, right = 0, min(a, b)
    res = 0
    while left <= right:
        mid = left + (right- left)//2 
        rem_a = a - mid
        rem_b = b - mid
        if rem_a+ rem_b >= mid* 2:
            res = mid
            left = mid + 1
        else:
            right = mid-1
            
    print(res)
"""
time complexity: O(logn)
space complexity: O(1)
"""
