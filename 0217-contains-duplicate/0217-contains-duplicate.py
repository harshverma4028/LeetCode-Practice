class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = set()

        for n in nums:
            if n not in l:
                l.add(n)
            else:
                return True  
        return False        