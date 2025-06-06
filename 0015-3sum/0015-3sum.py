class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 or not nums:
            return []

        nums.sort()
        hashs = set()    

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) -1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    hashs.add((nums[i],nums[left],nums[right]))
                    left +=1
                    right -=1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1            

        return list(hashs )           