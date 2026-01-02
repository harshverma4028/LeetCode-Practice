class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        res = []

        for c in nums1:
            if c in nums2 or c in nums3:
                if c not in res:
                    res.append(c)
            
        for c in nums2:
            if c in nums1 or c in nums3:
                if c not in res:
                    res.append(c)
        
        # for c in nums3:
        #     if c in nums1 or c in nums2:
        #         res.append(c)

        return res