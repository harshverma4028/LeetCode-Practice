class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # def calcsum(n):
        #     total = 0
        #     while n > 0:
        #         total += n % 10
        #         n //= 10
        #     return total

        # while num >= 10:
        #     num = calcsum(num)
        
        # return num

        if num == 0:
            return 0

        return 1 + (num - 1) % 9    