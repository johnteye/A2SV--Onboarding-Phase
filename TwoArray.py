
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    possible = True
    a.sort()
    b.sort()
    [-1, 0, 1]
    [0, 0, 2]
    for i in range(n):
        if a[i] != b[i] and a[i]+1 != b[i]:
            possible = False

            
            
    if possible:
        print("YES")
    else:
        print("NO")
  """
  time complexity:O(nlogn)
space complexity: O(1)
  """
