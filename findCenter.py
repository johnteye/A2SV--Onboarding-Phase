class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for key , val in edges:
            graph[key].append(val)
            graph[val].append(key)


        max_key = max(graph, key=lambda k: len(graph[k]))
        return max_key
        
