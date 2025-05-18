class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = {}
        for i,value in enumerate(nums):
            if value in my_dict:
                pasti = my_dict[value]
                if abs(pasti - i) <= k:
                    return True 

            my_dict[value] = i
        return False        
                 