class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 0:
            return 
        nums.sort()
        min_diff = float('inf')
        result = 0
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) -1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                elif abs(curr_sum - target) < min_diff:
                    min_diff = abs(curr_sum - target)  
                    result = curr_sum  

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1        

        return result