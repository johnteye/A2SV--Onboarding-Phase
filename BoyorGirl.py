name = str(input())
check = []
for char in name:
    if char not in check:
        check.append(char)
        
value = len(check)

if value% 2 == 1:
    print("IGNORE HIM!")
elif value % 2 == 0:
    print("CHAT WITH HER!")

"""
Time complexity: O(N)
Space complexity: O(1)
"""
