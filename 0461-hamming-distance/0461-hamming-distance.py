class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        count = 0
        while diff:
            if diff & 1:
                count += 1
            diff >>= 1    
        return count     