class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inr , dcr = 1, 1

        for i in range(1,len(nums)):
            inr &= nums[i] >= nums[i-1]
            dcr &= nums[i] <= nums[i-1]
        
        return bool(inr | dcr)


        # is_incr = True
        # is_dcr = True

        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         is_incr = False
        #     if nums[i] > nums[i-1]:
        #         is_dcr = False
        # return is_dcr or is_incr
        



        # def is_incr(nums):
        #     for i in range(1 ,len(nums)):
        #         if nums[i-1] > nums[i]:
        #             return False
        #     return True
        # def is_dcr(nums):
        #     for i in range(1, len(nums)):
        #         if nums[i-1] < nums[i]:
        #             return False
        #     return True

        # return is_incr(nums) or is_dcr(nums)