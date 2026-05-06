class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        res = []
        # res.append(nums[0])
        if len(nums) < 2:
            return nums

        for i in range(len(nums)):
            res.append(nums[i])
            if sum(res) > sum(nums[i+1:]):
                return res
            