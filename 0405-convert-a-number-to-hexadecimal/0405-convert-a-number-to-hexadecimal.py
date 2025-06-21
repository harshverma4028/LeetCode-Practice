class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        if num < 0:
            num = num & 0xFFFFFFFF

        hex_map = "0123456789abcdef"
        result = ""

        while num > 0:
            i = num % 16
            result += hex_map[i]
            num = num // 16

        return result[::-1]   
