class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest, start = 0, 0
        # hashmap = {}
        # for i, c in enumerate(s):
        #     if c in hashmap and start <= hashmap[c]:
        #         start = hashmap[c] + 1
        #     else:
        #         longest = max(longest, i-start+1)  
        #     hashmap[c] = i           
        # return longest 

        hashset = set()
        res = 0
        left = 0

        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[i])
            
            res = max(res, len(hashset))

        return res


        
        
