class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    
        new_k = k -1
        array = [i for i in range(1, n + 1)] #[1 2 3 4 5]

        index = 0
        while len(array) > 1:
            #for index in range(0, 2 * len(array)):
            #
            value = array[(index + new_k) % len(array)]
            rem_pos = (index + new_k) % len(array)
            array.remove(value)
            #[1 3 4 5]
            index = rem_pos
        for val in array:
            return val
    
      
      """
      Time Complexity:O(N2)
      Space Complexity: O(1)
      """
