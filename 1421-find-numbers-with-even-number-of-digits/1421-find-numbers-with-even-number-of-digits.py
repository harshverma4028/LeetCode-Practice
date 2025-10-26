class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0

        for i in range(len(nums)):
            chars = str(nums[i])
            if len(chars) % 2 == 0:
                even += 1

        return even