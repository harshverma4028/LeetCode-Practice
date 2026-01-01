class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {}

        for x in nums:
            if x-k in freq:
                count += freq[x-k]
            
            if x + k in freq:
                count += freq[x+k]
            
            if x in freq:
                freq[x] += 1
            
            else:
                freq[x] = 1




        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[i] - nums[j]) == k:
        #             count += 1
                
        return count