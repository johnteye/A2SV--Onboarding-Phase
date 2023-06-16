class Solution:
    def similarPairs(self, words: List[str]) -> int:        
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                word1 = set(words[i])
                word2 = set(words[j])
                if word1 == word2:
                    count += 1
        return count
      
      
    """
    Time Complexity: O(N2)
    Space Complexity:O(1)
    
    """
