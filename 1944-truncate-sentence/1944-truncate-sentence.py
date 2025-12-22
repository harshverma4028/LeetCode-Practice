class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # s = s.split()

        # ns = []
        # for i in range(k):
        #     ns.append(s[i])

        # return " ".join(ns)

        return " ".join(s.split()[:k])