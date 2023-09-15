class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        nums.append(float("-inf"))
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1] :
                left = mid + 1
            elif nums[mid -1] > nums[mid]:
                right = mid - 1
            else:
                return mid
        return 
