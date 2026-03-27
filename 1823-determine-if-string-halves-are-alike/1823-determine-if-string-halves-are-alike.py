class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        first = s[0:n//2]
        last = s[n//2:]

        vo = set("aeiouAEIOU")

        f = l = 0
        for c in first:
            if c in vo:
                f += 1

        for c in last:
            if c in vo:
                l += 1
            
        return f == l