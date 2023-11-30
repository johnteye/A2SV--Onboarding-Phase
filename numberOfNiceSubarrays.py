class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """

        count = 2
        res = 2
                        r
        nums = [1,1,2,1,1]
                  l

        """
        count = 0
        oddCount = 0
        res = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                oddCount += 1
                count = 0

            while oddCount == k:
                if nums[left] % 2 != 0:
                    oddCount -= 1
                
                count += 1
                left += 1
            res += count

        return res

