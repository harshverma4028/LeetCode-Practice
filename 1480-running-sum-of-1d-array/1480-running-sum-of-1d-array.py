class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(nums[i])
            else:
                temp = res[i-1]+ nums[i]
                res.append(temp)
        
        return res