      less =  ListNode(0)
        greater = ListNode(0)
        less_head = less
        greater_head = greater
        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        greater.next = None
        less.next = greater_head.next
        
        return less_head.next
