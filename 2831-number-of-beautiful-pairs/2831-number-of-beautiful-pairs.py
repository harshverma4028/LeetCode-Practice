class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        count = 0
        freq = [0] * 10
        
        for num in nums:
            last_digit = num % 10
            
            for first_digit in range(1, 10):
                if freq[first_digit] > 0:
                    if math.gcd(first_digit, last_digit) == 1:
                        count += freq[first_digit]
            
            first_digit = int(str(num)[0])
            freq[first_digit] += 1
            
        return count


        # import math
        # count = 0
        # n = len(nums)
        
        # for i in range(n):
        #     first_digit = int(str(nums[i])[0])
            
        #     for j in range(i + 1, n):
        #         last_digit = nums[j] % 10
                
        #         if math.gcd(first_digit, last_digit) == 1:
        #             count += 1
                    
        # return count
