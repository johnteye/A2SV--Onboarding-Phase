class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums = sorted(nums)
        for index, value in enumerate(nums):
            if value == target:
                res.append(index)

        return res

  """
  Time complexity: O(n)
  Space complexity: O(1)

  """
