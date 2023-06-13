class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
      """
      Time Complexity: O(N2)
      Space Complexity: O(1)
      """
