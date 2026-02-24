class Solution:
    def isFascinating(self, n: int) -> bool:
        
        t = str(n) + str(n*2) + str(n*3)
        # p = set()
        # if len(t) != 9 or '0' in t:
        #     return False
        # else:
        #     for s in t:
        #         if s in p:
        #             return False
        #         else:
        #             p.add(s)
                
        # return True

        return len(t) == 9 and set(t) == set("123456789")