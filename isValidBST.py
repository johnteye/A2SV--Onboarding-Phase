# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -math.inf, math.inf)

    def helper(self, node, low, high):
        if not node:
            return True

        if node.val >= high or node.val <= low:
            return False


        return self.helper(node.left, low, node.val) and self.helper(node.right, node.val,high)
