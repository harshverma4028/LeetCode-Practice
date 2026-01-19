class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []

        for n1 in nums1:
            if n1 not in nums2 and n1 not in res1:
                res1.append(n1)
                
        for n2 in nums2:
            if n2 not in nums1 and n2 not in res2:
                res2.append(n2)


        return [res1,res2]