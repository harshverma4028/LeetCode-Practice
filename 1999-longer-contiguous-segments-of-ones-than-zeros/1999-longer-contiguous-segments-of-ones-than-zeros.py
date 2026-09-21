class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        curr_one = 0
        curr_zero = 0
        one = 0
        zero = 0

        for char in s:
            if char == "1":
                curr_one += 1
                one = max(one , curr_one)
                curr_zero = 0
            else:
                curr_zero += 1
                zero = max(zero , curr_zero)
                curr_one = 0

        return one > zero