class MyQueue:

    def __init__(self):
        self.s1 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        return self.s1.pop(0)
        

    def peek(self) -> int:
        return self.s1[0]
        

    def empty(self) -> bool:
        return True if not self.s1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
