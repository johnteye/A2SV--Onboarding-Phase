# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        averages = []
        def bfs(root):
            
            while queue:

                curr_level = len(queue)
                total = 0

                for i in range(curr_level):
                    curr = queue.popleft()
                    total += curr.val
                    

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)


                averages.append(total/curr_level)

            return averages
    
        return bfs(root)
        
