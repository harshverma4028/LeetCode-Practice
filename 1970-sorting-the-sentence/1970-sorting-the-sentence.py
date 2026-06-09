class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        res = [None] * len(words)

        for word in words:
            i = int(word[-1]) - 1
            res[i] = word[:-1]

        return " ".join(res)