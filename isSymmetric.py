# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        def symmetry(t1, t2):
            if not t1 and not t2:
                return True
            
            if t1 and t2 and t1.val != t2.val:
                return False

            if (t1 and not t2) or (t2 and not t1):
                return False

            return symmetry(t1.right, t2.left) and symmetry(t1.left, t2.right)
        return symmetry(root.left, root.right) 
