n = int(input())
artifacts = list(map(int, input().split()))
artifacts.sort()
res = 1
for artifact in artifacts:
    if artifact > res:
        break
    res += artifact
print(res)

"""
time complexity: O(Nlogn)
space complexity: O(1)
"""
