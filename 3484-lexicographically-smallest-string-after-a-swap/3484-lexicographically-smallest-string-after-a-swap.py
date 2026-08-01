class Solution:
    def getSmallestString(self, s: str) -> str:
        
        arr = list(s)
        
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i] and (int(arr[i-1]) % 2 == int(arr[i]) % 2):
                arr[i-1] , arr[i] = arr[i] , arr[i-1]
                break
        
        return "".join(arr)