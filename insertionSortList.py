# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        
        new = ListNode(arr[0])
        curr2 = new
        for val in arr[1:]:
            curr2.next = ListNode(val)
            curr2 = curr2.next

        return new
