class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1

        for i in range(n -1):
            if nums[i+1] - nums[i] == 1:
                length = 2
                expected  = -1
            
                for j in range(i+1,n-1):
                    if nums[j+1] - nums[j] == expected:
                        length += 1
                        expected *= -1
                    else:
                        break

                ans = max(ans,length)
        return ans