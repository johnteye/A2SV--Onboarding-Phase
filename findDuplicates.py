class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                if i != correct_index:
                    duplicates.add(nums[i])
                i += 1
        return duplicates
        
