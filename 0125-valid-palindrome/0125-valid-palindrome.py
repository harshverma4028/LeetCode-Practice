import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i,j = 0,len(s)-1
        if len(s) == 1:
            return True
        while(i <= j):
            if s[i] != s[j]:
                return False
            i +=1
            j -=1
        return True   