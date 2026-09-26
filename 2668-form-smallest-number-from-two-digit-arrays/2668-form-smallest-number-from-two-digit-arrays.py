class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0

        nums1.sort()
        nums2.sort()

        common = list(set(nums1) & set(nums2))
        if common:
            return  min(common)
        else:
            a = nums1[0]
            b = nums2[0]

            if a < b:
                return a * 10 + b
            else:
                return b * 10 + a
