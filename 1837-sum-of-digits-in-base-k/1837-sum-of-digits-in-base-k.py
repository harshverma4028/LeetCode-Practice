class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        res = 0
        while 0 < n:
            digit = n % k
            n = n // k
            res += digit


        return res
