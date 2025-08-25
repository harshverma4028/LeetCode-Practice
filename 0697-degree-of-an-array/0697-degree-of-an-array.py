class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first , last , freq = {} , {} , {}

        for i,num in enumerate(nums):
            if num not in first:
                first[num] = i
            
            last[num] = i
            freq[num] = freq.get(num, 0) + 1

            degree = max(freq.values())
            min_len = float('inf')

        for num in freq:
            if freq[num] == degree:
                min_len = min(min_len, last[num] - first[num] + 1)

        return min_len