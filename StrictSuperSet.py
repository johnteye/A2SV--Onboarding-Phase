A = input().split()
B = []
n = int(input())
for _ in range(n):
    b = input().split()
    for element in b:
        B.append(element)

A, B = set(A), set(B)

res = A.issuperset(B)
print(res)
    
"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
