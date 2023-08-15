t = int(input())
from collections import defaultdict
for _ in range(t):
    n, c = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    count = defaultdict(int)
    
    ans = 0
    for i in range(n):
        count[arr[i]] += 1
        if count[arr[i]] <= c:
            ans += 1
            
    print(ans)
