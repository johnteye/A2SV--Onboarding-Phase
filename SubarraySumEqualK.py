class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        count = 0
        cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum - k in hashmap:
                count += hashmap[cum_sum-k]

            if cum_sum in hashmap:
                hashmap[cum_sum] += 1

            else:
                hashmap[cum_sum] = 1
        return count

"""
time complexity: O(n)
space complexity: O(1)
"""
