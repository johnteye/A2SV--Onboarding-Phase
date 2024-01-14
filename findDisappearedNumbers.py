class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i , n = 0, len(nums)
        res = []

        while i < n:
            curr = nums[i]
            correct_pos = curr - 1

            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
   

        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


        
