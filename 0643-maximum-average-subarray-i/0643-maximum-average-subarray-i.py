class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) <= k:
            return sum(nums) / float(k)

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k , len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(window_sum , max_sum)

        return max_sum / float(k)
