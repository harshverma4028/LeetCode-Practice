class Solution:
    def secondHighest(self, s: str) -> int:
        f = -1
        s_ = -1
        for char in s:
            if char.isnumeric():
                if int(char) > f:
                    s_ = f
                    f = int(char)
                elif f > int(char)  and s_  < int(char):
                    s_ = int(char) 
                
        return s_