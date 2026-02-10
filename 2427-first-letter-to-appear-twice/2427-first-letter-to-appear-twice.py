class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        l = set()
        for char in s:
            if char in l:
                return char
            else:
                l.add(char)


        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         if s[i] == s[j]:
        #             return s[i]