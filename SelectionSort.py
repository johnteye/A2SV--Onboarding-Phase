#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        return min_idx
                    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_idx = self.select(arr, i)
            arr[min_idx], arr[i] = arr[i] , arr[min_idx]
        return arr


"""
Time complexity: O(N2)
Space complexity: O(1)
"""
