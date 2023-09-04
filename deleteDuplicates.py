# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head.next
        slow = head
        while curr:
            if slow.val == curr.val:
                slow.next = curr.next

            else:
                slow = slow.next
            curr = curr.next
            

        return head
