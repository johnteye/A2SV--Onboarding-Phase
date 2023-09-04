class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        n = len(beans)

        diff = []
        for i in range(n):
            diff.append(total - (beans[i] * (n-i)))

        return min(diff)
