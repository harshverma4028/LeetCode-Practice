class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = b = 0

        for num in nums1:
            if num in set(nums2):
                a += 1
            
        for num in nums2:
            if num in set(nums1):
                b += 1
        
        return [a,b]