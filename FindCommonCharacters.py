class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for word in words[1:]:
            new_check = []
            for i in word:
                if i in check:
                    new_check.append(i)
                    check.remove(i)
            check = new_check
        return check
        
"""
Time Complexity:O(N2)
Space Complexity:O(1)
"""
