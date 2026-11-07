from typing import List
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        # s = set()
        # for sub in nums:
        #     l = sub[0]
        #     r = sub[1]
        #     while l <= r:
        #         s.add(l)
        #         l += 1

        # return len(s)

        a = [False] * 100

        nums.sort()

        total = 0
        start , end = nums[0]

        for s,e in nums[1:]:
            if s <= end:
                end = max(end , e)
            else:
                total += (end - start + 1)
                start, end = s, e
            
        total += (end - start + 1)
        return total