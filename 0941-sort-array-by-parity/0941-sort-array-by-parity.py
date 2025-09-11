from collections import deque

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0 , len(nums) - 1

        while left < right:
            if (nums[left]) & 1 == 0:
                left += 1
            elif (nums[right]) & 1 == 1:
                right -= 1
            else:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        return nums

        # new_list = deque([])
        # for i in range(len(nums)):
        #     if (nums[i] & 1) == 0:
        #         new_list.appendleft(nums[i])
        #     else:
        #         new_list.append(nums[i])

        # return list(new_list)

