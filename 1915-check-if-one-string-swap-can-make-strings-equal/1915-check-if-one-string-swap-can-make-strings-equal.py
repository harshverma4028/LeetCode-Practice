class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        most = 0
        if len(s1) != len(s2):
            return False
        i = 0
        dif = []
        while most < 3 and i < len(s1):
            if s1[i] != s2[i]:
                most += 1
                dif.append((s1[i],s2[i]))
            i += 1
        
        if len(dif) > 2:
            return False
        if len(dif) == 0:
            return True
        if len(dif) == 2:
            return dif[0][0] == dif[1][1] and dif[0][1] == dif[1][0]
        return False
