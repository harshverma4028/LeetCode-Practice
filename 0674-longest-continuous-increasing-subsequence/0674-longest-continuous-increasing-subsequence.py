class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = temp = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                temp +=1
                longest = max(longest, temp)
            else:
                temp = 1
        
        return longest