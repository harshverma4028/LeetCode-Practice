class Solution:
    def check(self, nums: List[int]) -> bool:
        ac = True

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if ac:
                    ac = False
                else:
                    return False
        if nums[0] < nums[-1]:
            if ac:
                ac = False
            else:
                return False

        return True