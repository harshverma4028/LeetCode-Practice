class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            ch = str(nums[i])
            for c in ch:
                res.append(int(c))

        return res