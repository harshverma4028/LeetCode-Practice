from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        res = []


        while  len(res) < len(s):

            for ch in sorted(count.keys()):
                if count[ch] > 0:
                    res.append(ch)
                    count[ch] -= 1
                
            
            for ch in sorted(count.keys(), reverse = True):
                if count[ch] > 0:
                    res.append(ch)
                    count[ch] -= 1
        

        return "".join(res)