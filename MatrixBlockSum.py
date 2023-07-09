class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows+ 1)]

        for i in range(rows):
            for j in range(cols):
                prefix[i +1][j + 1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] 

        answer = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                r1, c1 = max(0, i - k), max(0, j-k)
                r2, c2 = min(rows - 1, i + k), min(cols - 1, j+k)

                answer[i][j] = prefix[r2 + 1] [c2 + 1] - prefix[r2 + 1][c1] - prefix[r1][c2 + 1] + prefix[r1][c1]

        return answer
