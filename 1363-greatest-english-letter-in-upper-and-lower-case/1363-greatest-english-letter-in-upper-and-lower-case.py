class Solution:
    def greatestLetter(self, s: str) -> str:
        st = set(s)

        for c in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if c in st and c.lower() in st:
                return c

        # for ch in range(ord('Z'), ord('A') - 1, -1):
        #     c = chr(ch)
        #     if c in st and c.lower() in st:
        #         return c
                
        return ""