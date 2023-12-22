class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = defaultdict(set)
        indegree = defaultdict(int)
        queue = deque()
        res = []

        for i in range(n):
            indegree[i] = 0
            incoming[i] = set()

        for source , des in edges:
            graph[source].append(des)
            indegree[des] += 1
            incoming[des].add(source)

        for val in indegree:
            if indegree[val] == 0:
                queue.append(val)

        while queue:
            curr = queue.popleft()
            
            for income in incoming[curr]:
                incoming[curr] = incoming[curr].union(incoming[income])
                
            # for income in incoming[curr]:

            #     for val in incoming[income]:
            #         if val not in incoming[curr]:
            #             incoming[curr].append(val)

            # res.append(incoming[curr])
            #tle
            
            for neighbour in graph[curr]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        for val in incoming:
            res.append(sorted(incoming[val]))

        return res


        
