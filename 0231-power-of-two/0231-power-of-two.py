class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # i = 0
        # while (2**i <= n):
        #     if n == (2**i):
        #         return True
        #     i +=1
        # return False        
          
        if n < 1:
            return False
        elif n ==1 :
            return True
        else:
            while n%2 ==0:
                n = n // 2
            if n == 1:
                return True
            else:
                return False              

