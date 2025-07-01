class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # s = set(range(1,n + 1))
        

        # for char in nums:
        #     if char in s:
        #         s.remove(char)

        # return list(s)        

        for n in nums:
            i = abs(n) -1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res        

