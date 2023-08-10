t = int(input())
for _ in range(t):
    a, b, c = sorted(list(map(int, input().split())))
    results = []
    
    if a < c:
        a += 1
    if b < c:
        b += 1
    if b > a:
        b -= 1
    if c > a:
        c -=1
    
    results.append(abs(a-b) + abs(a-c) + abs(b-c))
    
    print(*results)
    
    
"""
Time complexity: O(1)
space complexity: O(1)
"""
