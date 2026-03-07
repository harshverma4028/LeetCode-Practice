class Solution:
    def maxSum(self, nums: List[int]) -> int:

        d = {}
        ans = -1

        for num in nums:
            m = max(str(num))
            
            if m in d:
                ans = max(ans, d[m] + num)
                d[m] = max(d[m], num)
            else:
                d[m] = num

        return ans