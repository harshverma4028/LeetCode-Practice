class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        rsum = (n *(n+1))/2
        sumt = 0
        for i in range(len(nums)):
            sumt += nums[i]
        return rsum - sumt 