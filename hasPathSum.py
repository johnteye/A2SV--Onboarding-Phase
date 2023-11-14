# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return
        def helper(node, path_sum):
            if not node:
                return

            if node.right is None and node.left is None:
                # helper(None, path_sum + node.val)
                # print(path_sum)
                return path_sum + node.val == targetSum
                
        
            left_call = helper(node.left, path_sum + node.val)
            right_call = helper(node.right, path_sum + node.val)

            return left_call or right_call


        
        return helper(root, 0)
