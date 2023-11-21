class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        hashmap = defaultdict(list)

        for num in nums:
            if hashmap[num-1]:
                heappush(hashmap[num], heappop(hashmap[num -1]) + 1 )

            else:
                heappush(hashmap[num], 1)

        return not any (length < 3 for length in sum(hashmap.values(), []))
        
