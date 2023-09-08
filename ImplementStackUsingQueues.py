class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        if not self.head:
            return
        res = self.head.val
        self.head = self.head.next

        return res

    def top(self) -> int:
        if not self.head:
            return
        res = self.head.val
        return res

    def empty(self) -> bool:
        if not self.head:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
