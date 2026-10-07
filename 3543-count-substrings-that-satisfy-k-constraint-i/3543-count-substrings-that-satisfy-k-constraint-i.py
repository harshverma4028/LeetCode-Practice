class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0 

        for i in range(len(s)):
            one = 0 
            zero = 0
            for j in range(i,len(s)):
                if s[j] == "0":
                    zero += 1
                else:
                    one += 1

                if zero <= k or one <= k:
                    res += 1
        return res