class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for step in range(1, n):
            key = nums[step]
            j = step - 1
            while j >=0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

        return nums

  """
  Time complexity: O(n)
  Space complexity: O(1)
  """
