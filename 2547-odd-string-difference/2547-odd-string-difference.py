class Solution:
    def oddString(self, words: List[str]) -> str:
        res = []

        for word in words:
            temp = []
            for i in range(len(word)-1):
                one = ord(word[i + 1]) - ord(word[i])
                temp.append(one)
            res.append(tuple(temp))
        
        count = Counter(res)

        for i in range(len(res)):
            if count[res[i]] == 1:
                return words[i]