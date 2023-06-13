n = int(input())
 
for test in range(n):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    
    max_widthA = max(a1, b1)
    max_widthB = max(a2, b2)
    
    min_widthA = min(a1, b1)
    min_widthB = min(a2, b2)
    
    for i in range(1):
        if min_widthA + a2 == max_widthA and max_widthA == max_widthB:
            print("Yes")
        elif min_widthA + b2 == max_widthA and max_widthA == max_widthB:
            print("Yes")
        else:
            print("No")
    
    """
    Time complexity : O(N)
    Space complexity: O(1)
    """
