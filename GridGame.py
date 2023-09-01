class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_top = grid[0].copy()
        prefix_down = grid[1].copy()
        for i in range(1, len(grid[0])):
            prefix_top[i] += prefix_top[i-1]
            prefix_down[i] += prefix_down[i-1]

        res = float("inf")
        for i in range(len(grid[0])):
            top = prefix_top[-1] - prefix_top[i]
            down = prefix_down[i-1] if i > 0 else 0
            second_robot = max(top, down)
            res = min(res, second_robot )

        return res
