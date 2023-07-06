n = int(input())
 
def mid(size):
    arr = [0]* size
    left, right = 0, size -1
    num = 0
    while left <= right:
        arr[left], arr[right] = num, num
        left +=1
        right -=1
        num += 1
    return arr
 
space_size = n
mid_size = 1
for i in range(n+1):
    print(*space_size*[" "], *mid(mid_size),*space_size*[" "])
    space_size -=1
    mid_size += 2
  
mid_size -= 4
space_size += 2
for j in range(n):
    print(*space_size*[" "], *mid(mid_size),*space_size*[" "])
    space_size += 1
    mid_size -= 2

""" Time complexity: O(n2)
Space complexity: O(1)
