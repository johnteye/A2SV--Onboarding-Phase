class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        def dfs(vertex, visited):
            
            visited.add(vertex)
            if vertex == destination:
                return True
                
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                   search = dfs(neighbour, visited)
                   
                   if search:
                       return True

            return False


        graph = defaultdict(list)
        visited = set()
        for key , val in edges:
            graph[key].append(val)
            graph[val].append(key)

        if not edges:
            return True
        
        return dfs(source, visited)
