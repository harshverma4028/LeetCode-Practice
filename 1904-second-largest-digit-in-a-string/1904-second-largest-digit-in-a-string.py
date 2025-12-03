class Solution:
    def secondHighest(self, s: str) -> int:
        f = -1
        s_ = -1
        for char in s:
            if char.isdigit():
                d = int(char)
                if d > f:
                    s_ = f
                    f = d
                elif f > d  > s_ :
                    s_ = d 
                
        return s_