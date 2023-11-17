class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap  = []
        # print(count)
        for key, val in count.items():
            heappush(heap, (-val, key))
        # print(heap)
        res = [heappop(heap)[1] for _ in range(k)]          
        # print(heap)
        return res
        


# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         count = Counter(words)
#         count = OrderedDict(count)
#         sorted_count = OrderedDict(sorted(count.items(), key=lambda x: (-x[1], x[0])))
#         res = []
#         # print(sorted_count)
#         for val in sorted_count:
#             res.append(val)
#             if len(res) == k:
#                 return res

#         return res
