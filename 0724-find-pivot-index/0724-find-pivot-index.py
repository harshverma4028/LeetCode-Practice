class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     left_sum = sum(nums[:i])
        #     right_sum = sum(nums[i+1:])

        #     if left_sum == right_sum:
        #         return i

        # return -1
        total_sum = sum(nums)
        left_sum = 0

        for i,num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i 
            
            left_sum += num
        
        return -1