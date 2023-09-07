class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(int(a) + int(b))
                elif i== "-":
                    stack.append(int(a) - int(b))
                elif i == "*":
                    stack.append(int(a) * int(b))
                else:
                    stack.append(int(a) / int(b))
            
            else:
                stack.append(int(i))
        return int(stack[-1])
