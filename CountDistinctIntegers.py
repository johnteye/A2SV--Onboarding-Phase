class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = []

        for val in nums:
            val = str(val)[::-1]
            res.append(int(val))
        
        nums.extend(res)
        return len(set(nums))

"""
Time complexity: O(N)
Space complexity: O(1)
"""
        
