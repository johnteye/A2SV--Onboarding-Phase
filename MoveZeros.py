class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for val in nums:
            if val == 0:
                temp = val
                nums.remove(val)
                nums.append(temp)

        return nums
      
      """
      Time Complexity: O(N)
      Space Complexity: O(1)
      """
