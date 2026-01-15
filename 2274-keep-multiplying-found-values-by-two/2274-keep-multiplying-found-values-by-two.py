class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = set(nums)

        while original in n:
            original *= 2

        return original

        # while True:
        #     if original not in n:
        #         return original
            
        #     original *= 2

