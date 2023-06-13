class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for val in range(0, n + 1):
            if val not in nums:
                return val
       

"""
Time Complexity: O(N),
Space Complexity: O(1)
"""
