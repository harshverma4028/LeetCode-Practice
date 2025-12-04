class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1)//2 - low//2

        # total = high - low + 1
        # if total % 2 == 0:
        #     return total//2
        
        # else:
        #     if high % 2 != 0 or low % 2 != 0:
        #         return (total//2) + 1
        #     else:
        #         return total//2
