class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        count = 0
        res = []
        check = Counter(p)
        # check the first 3 char of s
        subdict = {}
        if len(p) <= len(s): 
            for i in range(len(p)):
                if s[i] not in subdict:
                    subdict[s[i]] = 1
                else:
                    subdict[s[i]] += 1

        else:
            pass

        # make a right pointer to move from the end of the first subarray to the end of the string
        left = 0
        if subdict == check:
            count += 1
            res.append(left)

        for right in range(len(p), len(s)):
            if s[right] not in subdict:
                subdict[s[right]] = 1
            else:
                subdict[s[right]] += 1
            subdict[s[left]] -= 1
            if subdict[s[left]] <= 0:
                del subdict[s[left]]
            if subdict == check:
                count += 1
                res.append(left+1)
                
            left += 1
            
        return res

