class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        check = set()

        if sorted(s) == sorted(t):
            return True
        else:
            return False   

        # count = {}

        # for char in s:
        #     count[char] = count.get(char, 0) + 1

        # for char in t:
        #     if char not in count or count[char] == 0:
        #         return False
        #     count[char] -= 1

        
        # return all(v == 0 for v in count.values())
