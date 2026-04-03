class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        hi = 0

        for se in sentences:
            j = 1
            for i in se:
                if i == " ":
                    j += 1
                
            if j > hi:
                    hi = j
                
        return hi