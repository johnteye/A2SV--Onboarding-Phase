class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = float("inf")
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                start = min(mid, start)
                right = mid -1 
        left, right = 0, len(nums) -1
        end = float("-inf")
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                end = max(mid, end)
                left = mid +1 
        if end == float("-inf"):
            return [-1, -1]
        return [start, end]
    
