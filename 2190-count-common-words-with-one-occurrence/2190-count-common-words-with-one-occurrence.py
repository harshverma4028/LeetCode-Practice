class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = {}
        freq2 = {}

        for w in words1:
            if w not in freq1:
                freq1[w] = 1
            else:
                freq1[w] += 1

        for w in words2:
            if w not in freq2:
                freq2[w] = 1
            else:
                freq2[w] += 1

        count = 0
        for w in freq1:
            if freq1[w] == 1 and w in freq2 and freq2[w] == 1:
                count += 1

        return count