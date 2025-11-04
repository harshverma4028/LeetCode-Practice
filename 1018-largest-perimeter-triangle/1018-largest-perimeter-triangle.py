class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for k in range(len(nums) - 1, 1, -1):
            if nums[k-2] + nums[k-1] > nums[k]:
                return nums[k-2] + nums[k-1] + nums[k]
        
        return 0