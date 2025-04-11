class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                return count
            count +=1    
        return count