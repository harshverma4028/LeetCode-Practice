class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        ans = 0

        for i in range(n):
            left = i + 1
            right = n - i

            total_subarrays = left * right
            odd_subarrays = (total_subarrays + 1) // 2

            ans += arr[i] * odd_subarrays

        return ans


        # total_sum = 0
        # n = len(arr)
        
        # for i in range(n):
        #     for j in range(i,n):
        #         length = j - i + 1
        #         if length % 2 == 1:
        #             total_sum += sum(arr[i:j+1])
            
            
        # return total_sum