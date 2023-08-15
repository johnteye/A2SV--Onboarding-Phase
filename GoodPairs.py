t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    res1 = nums.index(min(nums)) + 1
    res2 = nums.index(max(nums)) + 1
    
    print(res1, res2)
