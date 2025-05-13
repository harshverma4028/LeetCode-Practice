class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            if n == 1:
                return True 

            visit.add(n)
            n = self.sumOfsquare(n)
       
        return False        

    def sumOfsquare(self,n):
        #
        output = 0
        while n:
            digit = n % 10 
            digit = digit ** 2
            output += digit
            n = n // 10
        return output    