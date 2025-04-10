class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =="":
            return 0

        for i in range(len(haystack) - len(needle)+1):
            part = haystack[i:i+len(needle)]

            if part == needle:
                return i 

        return -1
        # return haystack.find(needle)