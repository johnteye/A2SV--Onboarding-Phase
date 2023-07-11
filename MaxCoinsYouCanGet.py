class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)/3
        res = 0
        piles.sort()
        for i in range(int(n), len(piles), 2):
            res += piles[i]

        return res
"""
Time complexity: O(n)
Space complexity: O(1)

"""
