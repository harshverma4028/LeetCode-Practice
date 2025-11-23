class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lar = -1
        rec = {}
        for i in range(len(s)):
            if s[i] not in rec:
                rec[s[i]] = i
            else:
                lar = max(lar,(i -  rec[s[i]]-1))



        # for i in range(len(s)):
        #     for j in  range(i+1,len(s)):
        #         if s[i] == s[j]:
        #             lar = max(lar,( j - i)-1)

        return lar