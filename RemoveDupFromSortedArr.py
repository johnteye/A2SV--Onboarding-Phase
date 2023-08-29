class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                l += 1
                nums[l] = nums[r] 

        return l + 1

  """
time complexity: O(n0
space complexity: O(1)
  """
