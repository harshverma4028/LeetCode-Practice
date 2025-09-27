class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        count_parts, running_sum = 0, 0

        for i in range(len(arr)):
            running_sum += arr[i]

            if running_sum == target:
                count_parts += 1
                running_sum = 0

                if count_parts == 2 and i < len(arr) - 1:
                    return True

        return False
