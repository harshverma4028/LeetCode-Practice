class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        s = set()
        count = 0

        for char in words:
            if char[::-1] in s:
                count += 1
            else:
                s.add(char)

        return count