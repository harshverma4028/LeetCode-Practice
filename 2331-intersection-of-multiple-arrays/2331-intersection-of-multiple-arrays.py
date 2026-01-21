class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        common = set(nums[0])

        for arr in range(1,len(nums)):
            currentset = set(nums[arr])

            common = common.intersection(currentset)

        return sorted(list(common))