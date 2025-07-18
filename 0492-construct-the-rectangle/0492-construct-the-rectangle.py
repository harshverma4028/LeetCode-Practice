import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))

        while area % w != 0:
            w -=1
        l = area // w
        return [l,w]    
