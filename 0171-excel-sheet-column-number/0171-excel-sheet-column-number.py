class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        r = 0
        for char in columnTitle:
            r = r * 26 + (ord(char) - ord('A') + 1)
        return r 