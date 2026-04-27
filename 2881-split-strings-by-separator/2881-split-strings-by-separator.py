class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for word in words:
            parts = word.split(separator)
            
            for part in parts:
                if part != "":
                    res.append(part)
            
        return res