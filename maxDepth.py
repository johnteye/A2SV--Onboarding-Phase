"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, depth):
            if not root:
                return 0
            max_depth = 0
            for child in root.children:
                depth = dfs(child, depth + 1)

                if depth > max_depth:
                    max_depth = depth

                
            return max_depth + 1

        return dfs(root, 0)
