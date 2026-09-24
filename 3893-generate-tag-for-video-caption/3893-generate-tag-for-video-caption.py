class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()


        res = "#"


        for i in range(len(words)):
            if i == 0:
                res += words[i].lower()
            else:
                res += words[i].capitalize()

            if len(res) == 100:
                break

        return res[:100]