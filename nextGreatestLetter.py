class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        check = []

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                if not check:
                    check.append(letters[mid])
                else:
                    check[-1] = min(check[-1], letters[mid])
                right = mid - 1
                 
            elif letters[mid] <= target:
                left = mid + 1
        if check:
            return check[0]
        else:    
            return letters[0]
