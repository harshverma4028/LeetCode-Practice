class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """


        res = []
        i = 0

        while len(res) < len(arr):
            if arr[i] == 0 :
                res.append(0)
                if len(res) < len(arr):   
                    res.append(0)
            else:
                res.append(arr[i])
            i += 1
        
        for j in range(len(arr)):
            arr[j] = res[j]
