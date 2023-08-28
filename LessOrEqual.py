n, k = map(int,input().split())

a= list(map(int, input().split()))
a.sort()

if k == 0:
    if a[0] == 1:
        print("-1")
    else:
        print("1")
elif k == n:
    print(a[-1])
elif a[k-1] < a[k]:
    print(a[k-1])
else:
    print("-1")

"""
time complexity: O(nlogn)
space complexity: O(1)
"""
