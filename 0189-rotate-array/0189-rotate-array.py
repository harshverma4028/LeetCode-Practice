class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums.reverse()   # in-place reverse 
        nums[k:] = nums[k:][::-1]
        nums[:k] = nums[:k][::-1]

        
        # while k > 0:
        #     temp = nums[n-1]
        #     for i in range(n-1 , 0 , -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = temp
        #     k -= 1
        
