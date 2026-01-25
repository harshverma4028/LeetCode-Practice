from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        t_count = Counter(target)

        ans = float('inf')
        
        for ch in t_count:
            if ch not in s_count:
                return 0
            ans = min(ans, s_count[ch] // t_count[ch])

        return ans