# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_copy = copy.deepcopy(head)
        
        reversed_head = self.reverseList(head_copy)

        while head and reversed_head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next
        return True
        
