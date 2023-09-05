# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        i = 0
        twins = []
        while i <= ((n/2) - 1):
            twins.append(arr[i] + arr[n-1-i])
            i += 1
        return max(twins)

        
        
        
