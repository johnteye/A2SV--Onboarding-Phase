class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = []
        while left <= right:
            mid = left + (right - left)// 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)

            if total <= h:
                res.append(mid)
                right = mid -1
            else:
                left = mid +1
        
        return min(res)
"""
time complexity: O(nlogn)
space complexity: O(1)
"""
