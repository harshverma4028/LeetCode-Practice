from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_count  = Counter(t)
        s_count  = Counter(s)

        for char in t_count:
            if t_count[char] != s_count.get(char, 0):
                return char