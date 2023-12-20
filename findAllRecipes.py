class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        res = []

        for recipe in recipes:
            incoming[recipe] = 0

        for supply in supplies:
            incoming[supply] = 0

        for recipe in range(len(recipes)):
            for ing in ingredients[recipe]:
                graph[ing].append(recipes[recipe])
                incoming[recipes[recipe]] += 1

        for val in incoming:
            if incoming[val] == 0:
                queue.append(val)

        while queue:
            curr = queue.popleft()
            if curr not in supplies:
                res.append(curr)

            for neighbour in graph[curr]:
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)


        return res



        
