class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] = nums[i - 1] * 2
                del nums[i]
                nums.append(0)
 
        i, j = 0, 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1

        return nums
      
      """
      Time Complexity: O(N2)
      Spacce Complexity: O(1)
      """
