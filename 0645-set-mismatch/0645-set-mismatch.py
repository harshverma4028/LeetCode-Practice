class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        
        for i in range(n+ 1):
            if i not in seen:
                missing = i
        
        return [duplicate, missing]