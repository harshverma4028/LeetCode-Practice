class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i =0 
        j = 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i  += 1
            else:
                result.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j  += 1
        # print(result)
        n  = len(result)
        if n % 2 == 0:
            mid1 = n // 2-1
            mid2 = n // 2
            median = (result[mid1] + result[mid2]) / 2.0
            return median
        else :
            mid = n // 2
            return result[mid]
        