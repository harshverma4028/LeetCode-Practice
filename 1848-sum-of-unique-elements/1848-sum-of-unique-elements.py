class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        new = {}
        for i in range(len(nums)):
            if nums[i] not in new:
                new[nums[i]] = 1
            else:
                new[nums[i]] += 1
        res = 0
        for key , value in new.items():
            if value == 1:
                res += key
        
        return res