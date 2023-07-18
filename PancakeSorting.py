class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        sorted_arr = sorted(arr)
        res = []
        for i in range(n-1, -1, -1):
            if arr == sorted_arr:
                break

            j = arr.index(max(arr[:i+1]))
            if j != 0:
                arr[:j+1] = arr[:j+1][::-1]
                res.append(j+1)

            arr[:i+1] = arr[:i+1][::-1]
            res.append(i+1)

        return res
"""
time complexity: O(n)
space complexity: O(1)
"""
