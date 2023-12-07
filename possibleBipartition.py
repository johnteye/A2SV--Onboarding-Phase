class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node):
            for neighbour in graph[node]:
                if color[node] == color[neighbour]:
                    return False
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1

                    else:
                        color[neighbour] = 0
                    if not dfs(neighbour):
                        return False
            return True


        graph = defaultdict(list)
        for key, val in dislikes:
            graph[key].append(val)
            graph[val].append(key)
    
        result = True
        color = [-1 for _ in range(n+1)]
        for node in range(1, n+1):

            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node)
     
        
        return result



    
