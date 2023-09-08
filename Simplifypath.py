class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for direct in path.split('/'):
            if  direct == "..":
                if stack:
                    stack.pop()
            elif direct and direct != "." :
                stack.append(direct)

        
        string = ""
        print(stack)
        for val in stack:
            string += "/" + val
        if not stack:
            string = "/"
        return string
