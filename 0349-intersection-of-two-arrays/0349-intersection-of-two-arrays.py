class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set()
        num1 = set(nums1)

        for num in nums2:
            if num in num1:
                result.add(num)

        return list(result)        