class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = list()
        if nums is None:
            return [-1,-1]

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         ans.append(i)
        #         for j in range(i+1, len(nums)):
        #             if nums[j] != target:
        #                 ans.append(j-1)
        #                 return ans
        # return [-1,-1]                

        def findfirst(nums, target):
            left, right = 0 , len(nums)-1
            index = -1

            while left <= right:
                mid = (left + right) //  2

                if nums[mid] == target:
                    index = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid  - 1  

            return index
        def findlast(nums, target):
            left, right = 0 , len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid  - 1  

            return index             

        return [findfirst(nums,target), findlast(nums,target)]        