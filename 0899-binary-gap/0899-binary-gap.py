class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        binary = bin(n)[2:]

        ones = []
        for i,bit in enumerate(binary):
            if bit == '1':
                ones.append(i)

        for i in range(1 , len(ones)):
            max_gap = max(max_gap , ones[i] - ones[i -1])

        return max_gap
