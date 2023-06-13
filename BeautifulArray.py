n = int(input())
elements = list(map(int, input().split()))
 
negative, positive, zero = [], [], []
for elem in elements:
    if elem < 0:
        negative.append(elem)
    elif elem == 0:
        zero.append(elem)
    else:
        positive.append(elem)
        
if len(positive) == 0:
    positive.append(negative.pop())
    positive.append(negative.pop())
    
if len(negative) % 2 == 0:
    zero.append(negative.pop())
    
print(len(negative), *negative)
print(len(positive), * positive)
print(len(zero), *zero)

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
