class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        left = 0
        right = len(numbers) -1
    
        while left < right:
            
            s = numbers[left] + numbers[right]
            if  s == target:
                return [left+1,right+1]

            if s > target:
                right -= 1
            else:
                left += 1
            




        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if numbers[i] + numbers[j] == target:
        #             res.append(i+1)
        #             res.append(j+1)
        # return res