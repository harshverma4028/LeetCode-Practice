class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False

        for char in s:
            if char == '|':
                inside = not inside
            
            elif char == '*' and not inside:
                count += 1
            
        return count