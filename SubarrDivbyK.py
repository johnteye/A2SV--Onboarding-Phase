class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        for i in range(len(nums)):
            cum_sum += nums[i]

            if cum_sum % k in hashmap:
                count += hashmap[cum_sum%k]

            hashmap[cum_sum %k] += 1

        return count

