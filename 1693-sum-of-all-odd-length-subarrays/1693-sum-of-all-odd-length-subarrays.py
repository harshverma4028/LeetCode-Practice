class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i,n):
                length = j - i + 1
                if length % 2 == 1:
                    total_sum += sum(arr[i:j+1])
            
            
        return total_sum