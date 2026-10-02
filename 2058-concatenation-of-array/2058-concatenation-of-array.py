class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = nums.copy()

        res.extend(nums)

        return res