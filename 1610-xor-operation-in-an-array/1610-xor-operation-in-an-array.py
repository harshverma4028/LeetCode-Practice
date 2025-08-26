class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        rs = 0
        for i in range(n):
            rs ^= start + 2 * i

        return rs            