class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        n = len(pref)

        for i in range(len(words)):
            if words[i][:n] == pref:
                res += 1

            
        return res