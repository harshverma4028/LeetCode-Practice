class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = set()
        visited.add((0,0))
        for chr in path:
            if chr == "N":
                y += 1
            elif chr == "S":
                y -= 1
            elif chr == "E":
                x += 1
            elif chr == "W":
                x -= 1
            
            if ((x,y)) in visited:
                return True

            visited.add((x,y))
        
        return False