def destroy():
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = [0] * (max(arr) + 1)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        if count[i - 1] < count[i]:
            print("NO")
            return
        
    print("YES")

t = int(input())
for _ in range(t):
    destroy()

"""
Time complexity: O(n)
Space complexity: O(n)

"""
