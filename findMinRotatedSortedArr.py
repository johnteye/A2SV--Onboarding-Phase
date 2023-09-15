class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        left , right = 0, len(nums) - 1
        low = float("inf")
        while left <=right:
            mid = left + (right - left)// 2
            low = min(low, nums[mid])
            if nums[mid] > last:
                left = mid + 1
            else:
                right = mid-1

        return low

  """
time complexity: O(log n)
space complexity: O(1)
  """
