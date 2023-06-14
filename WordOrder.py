# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n= int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

word_val = []
word_count = Counter(words)
print(len(word_count))
for val in word_count:
    word_val.append(word_count[val])
print(*word_val)

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
