class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        table = [1] * n

        table[0] = 0
        table[1] = 0

        for i in range(2, int(sqrt(n)) + 1):
            if table[i]:
                for j in range(i * i, n, i):
                    table[j] = 0
        
        return sum(table)
        
