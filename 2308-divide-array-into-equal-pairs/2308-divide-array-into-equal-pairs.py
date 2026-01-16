class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        for val in freq.values():
            if val % 2 == 1:
                return False
            
        return True