class Solution:
    def isBalanced(self, num: str) -> bool:
        even = odd = 0

        for i, ch in enumerate(num):
            if i % 2 == 0:
                even += int(ch)
            else:
                odd += int(ch)


        return even == odd