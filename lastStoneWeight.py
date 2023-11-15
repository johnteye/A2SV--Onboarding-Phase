class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapify(stones)
        while len(stones) > 1:

            y = -heappop(stones)
            x = -heappop(stones)
            print(x,y)
            if x != y:
                val = y - x
                heappush(stones, -val)

        
        if not stones:
            return 0
        return abs(stones[0])



