class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]

                start += 1
                end -=1

        k = k % len(nums)
        left, right = 0, len(nums) -1

        rotate(left, right)
        rotate(left, k-1)
        rotate(k, right)

  
