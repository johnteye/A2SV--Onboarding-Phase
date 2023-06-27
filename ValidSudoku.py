class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for row_idx in range(9):
            for col_idx in range(9):
                element = board[row_idx][col_idx]
                if element != ".":
                    res += [(row_idx, element), (element, col_idx), (row_idx//3, col_idx//3, element)]

        return len(res) == len(set(res))


"""
Time Complexity: O(N2)
Space Complexity: O(1)

"""
