class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)

        return len(s) == 0


        # freq = {}
        # for i in range(len(nums)):
        #     if nums[i] not in freq:
        #         freq[nums[i]] = 1
        #     else:
        #         freq[nums[i]] += 1
        
        # for val in freq.values():
        #     if val % 2 == 1:
        #         return False
            
        # return True