class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        collections = []

        def backtrack(i, collection):
            if len(collection) == k:
                collections.append(collection.copy())
                return 

            if i >=  n:
                return

            collection.append(nums[i])
            backtrack(i+1, collection)
            collection.pop()
            #print(i)
            
            backtrack(i+1, collection)

        backtrack(0, [])
        return collections
