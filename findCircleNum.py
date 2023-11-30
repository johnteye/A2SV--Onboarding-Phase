class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    graph[row].append(col)

    
        def dfs(city, visited):
            visited.add(city)
            for neighbour in graph[city]:
                if neighbour not in visited:
                    dfs(neighbour, visited)

        province_count = 0
                
        for city in graph:
            if city not in visited: 
                dfs(city, visited) 
                province_count += 1

        return province_count
