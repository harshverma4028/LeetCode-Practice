class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left , right = 0, 1
        result = 0
        while right < len(nums):
            diff = nums[right] - nums[left]
            if diff == 1:
                result = max(result, right - left + 1)
            if diff <= 1:
                right += 1
            else:
                left += 1
    
        return result