class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                if matrix[row_idx][col_idx] == target:
                    return True
        return False
                
        
    """
    Time Complexity: O(N2)
    Space Complexity: O(1)
    """
