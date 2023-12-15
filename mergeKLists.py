# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(lists)):
            while lists[i]:

                heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        
        
        while heap:

            head = ListNode(heappop(heap))
            curr.next = head
            curr = curr.next


        return dummy.next
