import string
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(len(s)):
            if s[i] != '?':
                continue

            left = s[i-1] if i > 0 else None
            right = s[i+1] if i < n-1 and s[i+1] != '?' else None

            for char in string.ascii_lowercase:
                if char != left and char != right:
                    s[i] = char
                    break

            
        return "".join(s)