n = int(input())
arr = list(map(int, input().split()))
 
flag = False
start = 0
end = 0
for i in range(1, n):
    if arr[i-1] > arr[i] and not flag:
        start = i - 1
        flag = True
        
    if arr[start] > arr[i]:
        end = i
        
 
# new_arr = list(reversed(arr[start: end + 1]))
# new_arr = new_arr + arr[end+1:]
new_arr = arr[:start] + list(reversed(arr[start:end+1])) + arr[end+1:]
 
if new_arr == sorted(arr):
    print("yes")
    print(start+1, end+ 1)
else:
    print("no")

"""
Time complexity: O(n)
space complexity: O(1)
"""
