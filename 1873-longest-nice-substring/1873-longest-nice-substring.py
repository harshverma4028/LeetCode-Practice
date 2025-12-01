class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ""

        def isNice(sub):
            for c in sub:
                if c.islower() and c.upper() not in sub:
                    return False
                if c.isupper() and c.lower() not in sub:
                    return False
            return True

        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if isNice(sub) and len(sub) > len(res):
                    res = sub
        
        return res
