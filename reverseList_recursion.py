# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if not head:
            return
        if head.next is None:
            return head

        newHead =  self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return newHead
