class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        collections = []
        n = len(nums)
        def backtrack(i, collection):
            if collection not in collections:
                collections.append(collection[:])

            if i >= n:
                return

            collection.append(nums[i])
            backtrack(i+1,collection)
            collection.pop()


            backtrack(i+1, collection)


        backtrack(0, [])
        return collections
