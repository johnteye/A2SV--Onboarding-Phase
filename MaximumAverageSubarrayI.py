class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float("-inf")
        sums = 0
        left = 0
        for i in range(k):
            sums += nums[i]

        maxi = max(maxi, sums/k)

        for right in range(k, len(nums)):
            sums += nums[right]
            sums -= nums[left]
            maxi = max(maxi, sums/k)

            left += 1

        return maxi
