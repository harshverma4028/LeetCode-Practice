class Solution(object):
    def convertToBase7(self,num):
        if num == 0:
            return "0"

        isNegative = False
        if num < 0:
            isNegative = True
            num = abs(num)

        result = ""

        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num = num // 7

        if isNegative:
            result = "-" + result

        return result
