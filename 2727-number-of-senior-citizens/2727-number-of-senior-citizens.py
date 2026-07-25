class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for l in details:
            if int(l[-4:-2]) > 60:
                res += 1
        
        return res
