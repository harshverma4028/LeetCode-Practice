from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num) - 1
        carry = 0

        while n >= 0 or k > 0 or carry > 0:
            digit = (num[n] if n >= 0 else 0) + (k % 10) + carry

            if n >= 0:
                num[n] = digit % 10
            else:
                num.insert(0, digit % 10)

            carry = digit // 10
            k //= 10
            n -= 1

        return num
