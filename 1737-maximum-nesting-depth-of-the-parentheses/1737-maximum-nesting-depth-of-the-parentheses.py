class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        c_d = 0
        o = '('
        c = ')'

        for char in s:
            if char == o:
                c_d += 1
                if c_d > depth:
                    depth = c_d

            elif char == c:
                c_d -= 1

        return depth
