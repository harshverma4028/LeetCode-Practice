class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        group = {"electronics", "grocery", "pharmacy", "restaurant"}
        res = []
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        for i in range(len(code)):
            if not isActive[i]:
                continue

            if businessLine[i] not in group:
                continue

            if not code[i]:
                continue

            if all(ch.isalnum() or ch == "_" for ch in code[i]):
                res.append((order[businessLine[i]], code[i]))
        
        res.sort() 
        return [c for _, c in res]