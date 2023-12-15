class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def moves(pos):
            res = []
            for i in range(len(pos)):
                
                pos_new = pos[:i] +  str((int(pos[i]) + 1) % 10) + pos[i+1:]
                res.append(pos_new)
               
                pos_new = pos[:i] +  str((int(pos[i]) - 1 ) % 10) + pos[i+1:]
                res.append(pos_new)
                
            return res

    
        start = ("0000", 0)
        queue = deque([start])
        visited = set()

        if start[0] in deadends:
            return -1
            
        while queue:
            curr, step = queue.popleft()
            if curr == target:
                return step

            for move in moves(curr):
                if move not in deadends and move not in visited:
                    visited.add(move)
                    queue.append((move, step+1))

        return -1
