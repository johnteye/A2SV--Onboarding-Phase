# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        curr1 = l1
        curr2 = l2
        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next
        str1 = int(str1[::-1])
        str2 = int(str2[::-1])

        res = str1 + str2
        res = str(res)
        res = res[::-1]
        res = list(map(int, res))
        
        head = ListNode(int(res[0]))
        curr = head

        # Create a new ListNode for each remaining digit and link them together
        for digit in res[1:]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return head
