class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(1, 0),(-1, 0), (0, 1), (0, -1)]

        start = image[sr][sc]
        visited = []
            
        image[sr][sc] = color

        def inbound(new_dir):
            if  0 <= new_dir[0] < len(image) and 0 <= new_dir[1]< len(image[0]):
                return True

            return False



        def dfs(cell, visited):
            visited.append(cell)

            # print(cell)

            for dir in dirs:
                new_dir = [dir[0]+cell[0], dir[1]+cell[1]]
                if inbound(new_dir) and new_dir not in visited:
                   
                    if image[new_dir[0]][new_dir[1]] == start:
                        print([new_dir[0]],[new_dir[1]] )
                        image[new_dir[0]][new_dir[1]] = color
                        dfs(new_dir, visited)
                    


        
        dfs([sr,sc], visited)
        return image
                    
