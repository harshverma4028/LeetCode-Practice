class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = set(nums)

        while True:
            if original not in n:
                return original
            
            original *= 2

