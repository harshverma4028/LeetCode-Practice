class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        while i <= len(s)//2:
            if s[i] != s[n-i-1]:
                if ord(s[i]) < ord(s[n-i-1]):
                    s[n-i-1] = s[i]
                else:
                    s[i] = s[n-i-1]
                
            i += 1
    
        return "".join(s)