class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
        
        # if n % 4 == 0:
        #     return False
        # else:
        #     return True            