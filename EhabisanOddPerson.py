n = int(input())
arr = list(map(int, input().split()))


if any(x % 2 == 1 for x in arr) and any(x % 2 == 0 for x in arr):
    arr.sort()
        
print(*arr)

"""
time complexity: O(nlogn)
space complexity: O(1)
"""
