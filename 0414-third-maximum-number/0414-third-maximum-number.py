class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums)) 
        # nums.sort(reverse = True)

        # if len(nums) < 3 :
        #     return nums[0]
        # else:
        #     return nums[2]  

        f = s = t = float('-inf') 

        for num in nums:
            if num == f or num == s or num == t:
                continue
            elif num > f:
                t = s
                s = f 
                f = num
            elif num > s:
                t = s
                s = num
            elif num > t:
                t = num
        return f if t == float('-inf') else t                    
