from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s3  = s1.split() + s2.split()

        frequency_map = Counter(s3)

        return [word for word,freq in frequency_map.items() if freq == 1]

        # res  = []
        # frequency_map = {}

        # for item in s3:
        #     if item in frequency_map:
        #         frequency_map[item] += 1
        #     else:
        #         frequency_map[item] = 1


        # for item in s3:
        #     if frequency_map[item] == 1:
        #         res.append(item)

        # return res
