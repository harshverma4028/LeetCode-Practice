class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        min_length = min(len(word1),len(word2))

        l = r = 0

        while l < len(word1) or r < len(word2):
            if l < len(word1):
                merged.append(word1[l])
                l += 1
            
            if r < len(word2):
                merged.append(word2[r])
                r += 1
            

        return "".join(merged)