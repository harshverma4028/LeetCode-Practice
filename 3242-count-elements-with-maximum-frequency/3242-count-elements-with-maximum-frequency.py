
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_freq = 0

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]

        ans = 0

        for num in freq:
            if freq[num] == max_freq:
                ans += freq[num]

        return ans