class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        candidates = [arr[n // 4], arr[n // 2], arr[(3 * n) // 4]]

        for value in candidates:
            first_index = -1
            last_index = -1

            for i in range(n):
                if arr[i] == value:
                    if first_index == -1:
                        first_index = i
                    last_index = i

            freq = last_index - first_index + 1
            if freq > n//4:
                return value
