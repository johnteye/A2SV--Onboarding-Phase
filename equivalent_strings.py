 
from functools import lru_cache


@lru_cache 
def fn(str1, str2):
    
  #base case
  if str1 == str2:
      return True
  if len(str1) % 2 != 0:
      return False

  mid = len(str1) // 2
  a1 = str1[:mid]
  a2 = str1[mid:]
  
  b1 = str2[:mid]
  b2 = str2[mid:]
  
  return (fn(a1, b1) and fn(a2, b2)) or (fn(a1, b2) and fn(a2, b1))
  
  
str1 = str(input())
str2 = str(input())

res = fn(str1, str2)
if res:
    print("YES")
else:
    print("NO")
