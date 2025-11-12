class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        first_index  = {}
        values = sorted(nums)
        for i, v in enumerate(values):
            if v not in first_index:      # store first occurrence only
                first_index[v] = i
        
        for x in nums:
            res.append(first_index[x])
        
        return res


        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
            
        #     res.append(count)

        # return res