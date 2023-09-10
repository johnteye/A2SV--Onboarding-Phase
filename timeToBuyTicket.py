class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        left, right =0,  len(tickets)
        count = 0
        while tickets[k] != 0:
            if tickets[left]>0:
                tickets[left] -= 1
                count += 1
            left += 1
            if left == right:
                left = 0
        return count
