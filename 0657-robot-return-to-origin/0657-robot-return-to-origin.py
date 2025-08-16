class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # l=r=d=u = 0
        # for char in moves:
        #     if char == 'L':
        #         l += 1
        #     elif char == 'U':
        #         u += 1
        #     elif char == 'R':
        #         r += 1
        #     elif char == 'D':
        #         d += 1
            
        # return u == d and l == r

        x = y = 0
        for char in moves:
            if char == 'L': x -= 1
            elif char == 'U': y += 1
            elif char == 'R': x += 1
            elif char == 'D': y -= 1

        return x == 0 and y == 0
