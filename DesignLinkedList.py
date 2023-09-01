class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        
        # if not self.head:
        #     return 
        find = 0
        curr = self.head
        while curr:
            if find == index:
                return curr.val
            curr = curr.next
            find += 1
        return -1

    def addAtHead(self, val: int) -> None:
        # if self.head is None:
        #     new_node =  Node(val)
        #     self.head = new_node
        #     return 
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return 
        new_node = Node(val)
        find = 0
        curr = self.head
        while curr:
            if find == index -1:
                new_node.next = curr.next
                curr.next = new_node
            curr = curr.next
            find += 1

    def deleteAtIndex(self, index: int) -> None:
        if index ==0:
            if self.head:
                self.head = self.head.next
        
        pos = 0
        curr = self.head
        while curr:
            if pos == index-1 and curr.next:
                curr.next = curr.next.next
            curr = curr.next
            pos += 1
        
    # def print(self):
    #     temp = self.head
    #     while temp and temp.next:
    #         print(temp.val,end ='->')
    #         temp = temp.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
