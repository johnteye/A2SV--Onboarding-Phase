class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        total =  10
                    r
        nums = [2,3,1,2,4,3] target = 7
                l 
    
        if total + right > target:
            find min(res)
            total -= left
        
        """

        total = 0
        left = 0 
        res = float("inf")


        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        if res != float("inf"):
            return res

        return 0
