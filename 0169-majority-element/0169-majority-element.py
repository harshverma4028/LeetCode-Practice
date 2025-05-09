class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = 0
        count = 0
        # for i in range(0,len(nums)-1):
        #     if count == 0:
        #         cand = nums[i]
        #     if cand == nums[i]:
        #         count +=1
        # return cand            
        for num in nums:
            if count == 0:
                cand = num
            count += (1 if num == cand else -1 )  
        return cand    