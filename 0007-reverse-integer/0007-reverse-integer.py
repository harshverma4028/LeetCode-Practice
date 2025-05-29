class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)

        while(x != 0):
            digit = x % 10

            rev = (rev * 10) + digit

            x = x // 10

        rev = rev * sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev   