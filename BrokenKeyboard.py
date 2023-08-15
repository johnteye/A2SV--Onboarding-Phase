from collections import Counter
t = int(input())
for _ in range(t):
    keys = input()
    res = ""
    i = 0
    while i < len(keys):
        if i + 1 < len(keys) and keys[i] == keys[i + 1]:
            i += 1
        else:
            res += keys[i]
       
        i += 1
    res = sorted(set(res))
    print("".join(res))
