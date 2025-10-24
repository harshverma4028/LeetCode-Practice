class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        res = []
        for i in range(len(words)-1):
            curr_word = words[i]
            for j in range(i+1,len(words)):
                if curr_word in words[j]:
                    res.append(curr_word)
                    break

        return res