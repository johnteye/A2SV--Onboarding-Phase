class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
      
      """
      Time Complexity:O(N)
      Space Complexity: O(1)
      """
