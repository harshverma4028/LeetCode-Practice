class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        f = freq[s[0]]

        for val in freq.values():
            if val != f:
                return False
        
        return True