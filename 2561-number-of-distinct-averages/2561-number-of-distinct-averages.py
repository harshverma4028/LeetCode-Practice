class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        i , j = 0 , len(nums)-1
        average = set()

        while i < j:
            avg = (nums[i] + nums[j]) / 2 
            average.add(avg)

            i += 1
            j -= 1

        return len(average)
