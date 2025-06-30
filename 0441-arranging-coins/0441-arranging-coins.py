class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row -1    
    