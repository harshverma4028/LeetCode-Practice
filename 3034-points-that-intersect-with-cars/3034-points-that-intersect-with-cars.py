class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()

        for sub in nums:
            l = sub[0]
            r = sub[1]
            while l <= r:
                s.add(l)
                l += 1

            
        return len(s)