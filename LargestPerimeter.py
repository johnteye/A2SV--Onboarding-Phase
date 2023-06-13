class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)

        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if b + c > a:
                return a + b + c

        return 0
      
      """
      Time complexity: O(N)
      Space complexity: O(1)
      """
