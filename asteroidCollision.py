class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)

            else:
                while ast:
                    if not stack or stack[-1] < 0:
                        stack.append(ast)
                        ast = 0
                    elif abs(ast) < stack[-1]:
                        ast = 0
                    elif abs(ast) == stack[-1]:
                        stack.pop()
                        ast = 0
                    elif abs(ast) > stack[-1]:
                        stack.pop()

        return stack

        
        
        
        
        
        """  stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
"""
