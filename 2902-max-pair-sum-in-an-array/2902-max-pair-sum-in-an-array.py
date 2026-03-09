class Solution:
    def maxSum(self, nums: List[int]) -> int:


        ans = -1
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):

                if max(str(nums[i])) == max(str(nums[j])):
                    ans = max(ans, nums[i] + nums[j])

        return ans


        ## optimal approach

        # d = {}
        # ans = -1

        # for num in nums:
        #     m = max(str(num))
            
        #     if m in d:
        #         ans = max(ans, d[m] + num)
        #         d[m] = max(d[m], num)
        #     else:
        #         d[m] = num

        # return ans