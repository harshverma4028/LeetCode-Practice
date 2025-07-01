class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set(range(1,n + 1))
        

        for char in nums:
            if char in s:
                s.remove(char)

        return list(s)        

        

