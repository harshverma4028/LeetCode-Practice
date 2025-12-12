class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        l = []
        count = 0

        for i in range(len(s)-1,-1,-1):
            if count == 3:
                count = 0
                l.append(".")
            count += 1
            l.append(s[i])

        l.reverse()
        return "".join(l)
