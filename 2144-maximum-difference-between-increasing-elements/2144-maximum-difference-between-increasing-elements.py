class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = -1

        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    m = max(nums[j] - nums[i],m)
        return m
