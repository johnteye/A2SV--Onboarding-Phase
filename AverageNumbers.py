n = int(input())
arr = list(map(int,input().split()))
 
mean = sum(arr)/len(arr)
res = []
count = 0
for index, val in enumerate(arr):
    if val == mean:
        res.append(index+ 1)
        count += 1
else:     
    print(count)       
    print(*res)

"""
Time complexity: O(N)
Space complexity: O(1)
"""
