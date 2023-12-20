class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = defaultdict(int)
        graf = defaultdict(list)
        queue = deque()
        res = []

        for j in range(len(graph)):
            outgoing[j] = 0

        for i in range(len(graph)):
            for node in graph[i]:
                graf[node].append(i)
                outgoing[i] +=1

        for val in outgoing:
            if outgoing[val] == 0:
                queue.append(val)


        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbour in graf[curr]:
                outgoing[neighbour] -= 1

                if outgoing[neighbour] == 0:
                    queue.append(neighbour)

        return sorted(res)
            
        
