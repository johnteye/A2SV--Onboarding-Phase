class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
                i
        0[1,0]0

        

        """
        leng =  len(flowerbed)
        flowerbed = [0]+ flowerbed + [0]
        count = 0
        for flower in range(1, leng+ 1):
            if flowerbed[flower] == 0 and flowerbed[flower-1] == 0 and flowerbed[flower+1] ==0:
                count += 1
                flowerbed[flower] = 1

        if count >= n:
            return True
        return False
