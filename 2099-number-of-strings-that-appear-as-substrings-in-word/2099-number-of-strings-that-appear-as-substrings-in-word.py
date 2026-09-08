class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for char in patterns:
            if char in word:
                res += 1
        
        return res