class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s:
            if 'A' <= c <= 'Z':
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)
        return "".join(result)