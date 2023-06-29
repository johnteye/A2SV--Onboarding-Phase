class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # bubble sort
        '''
        size = len(heights)
        for i in range(size):
            for j in range(size - i - 1):
                if heights[j] < heights[j+ 1]:
                    heights[j], heights[j + 1] = heights[j+ 1], heights[j]
                    names[j], names[j+ 1] = names[j+1], names[j]


        return names
        '''

        # selection sort
        size = len(heights)
        for i in range(size):
            max_idx = i
            for j in range(i + 1, size):
                if heights[max_idx] < heights[j]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx] , heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]

        return names

"""
Time complexity: O(N2)
Space complexity: O(1)
"""
