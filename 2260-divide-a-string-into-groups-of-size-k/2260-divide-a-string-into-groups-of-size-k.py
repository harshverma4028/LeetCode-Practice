from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        
        rem = len(s) % k
        if rem != 0:
            s += fill * (k - rem)
        
        for i in range(0, len(s), k):
            res.append(s[i:i+k])
        
        return res