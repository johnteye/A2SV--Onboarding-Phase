class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        def sumsquare(left, right):
            return (right* right) + (left * left)

        while left <= right:
            if sumsquare(left, right)> c:
                right -= 1
            elif sumsquare(left, right) < c:
                left += 1

            else:
                return True

        return False


            
