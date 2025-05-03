class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = 0
        for num in nums:
            value ^= num
        return value    