class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = 0
        for i in range(len(nums)):
            if nums[largest] < nums[i]:
                largest = i

        for i in range(len(nums)):
            if i == largest:
                continue
            if nums[i] * 2 > nums[largest]:
                return -1
            

        return largest