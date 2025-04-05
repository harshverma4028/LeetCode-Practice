class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_str = str(x)
        start = 0
        end = len(x_str) - 1

        while start < end:
            if x_str[start] != x_str[end]:
                return False
            start +=1
            end  -= 1

        return True        

        