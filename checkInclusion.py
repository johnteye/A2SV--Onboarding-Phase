class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        check = Counter(s1)
        # check the first 3 char of s
        subdict = {}
        if len(s1) <= len(s2): 
            for i in range(len(s1)):
                if s2[i] not in subdict:
                    subdict[s2[i]] = 1
                else:
                    subdict[s2[i]] += 1

        else:
            pass

        # make a right pointer to move from the end of the first subarray to the end of the string
        left = 0
        if subdict == check:
            return True
            

        for right in range(len(s1), len(s2)):
            if s2[right] not in subdict:
                subdict[s2[right]] = 1
            else:
                subdict[s2[right]] += 1
            subdict[s2[left]] -= 1
            if subdict[s2[left]] <= 0:
                del subdict[s2[left]]
            if subdict == check:
                return True
            left += 1
            
        return False
