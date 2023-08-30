class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        values = []
        for i in s:
            values.append(ord(i) - 97)
        shifts = shifts[::-1]
        prefix = [0]* len(shifts)
        prefix[0] = shifts[0]
        for i in range(1,len(shifts)):
            prefix[i] = prefix[i-1] + shifts[i]
        prefix =  prefix[::-1]
        
        for i in range(len(values)):
            values[i] += prefix[i]
            values[i] %= 26
  
                
        res = ""
        for val in values:
            test = val + 97
            res +=chr(test)
        return res


"""
time complexity: O(n)
space complexity: O(n)
"""
