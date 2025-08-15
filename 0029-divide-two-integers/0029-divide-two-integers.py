class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        while dvd >= dvs:
            temp = dvs
            multiple = 1

            while (temp << 1) <= dvd:
                temp <<= 1
                multiple <<= 1

            dvd -= temp
            quotient += multiple

        return sign * quotient