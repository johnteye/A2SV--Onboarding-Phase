class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i , n = 0, len(nums)

        while i < n:
            curr = nums[i]

            if curr < n and curr != i:
                nums[curr], nums[i] = nums[i],  nums[curr]

            else:
                i += 1

        

        return next((i for i in range(n) if nums[i] != i), n)
        
