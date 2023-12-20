class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degrees = defaultdict(int)
        for i in range(numCourses):
            degrees[i] =  0 
        queue = deque()
        res = []
        # graph{0: [1, 2], 1: [3] 2: [3] }
        #degrees(0: 0, 1: 1, 2: 1 , 3: 2)
        #queue = [1, 2]
        # curr = 
        #res = [0, ]
        

        for course, preq in prerequisites:
            graph[preq].append(course)
            degrees[course] += 1

        for degree in degrees:
            if degrees[degree] == 0 :
                queue.append(degree)

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbour in graph[curr]:
                degrees[neighbour] -= 1

                if degrees[neighbour] == 0:
                    queue.append(neighbour)




        if len(res) == numCourses:
            return res
        return []




        
