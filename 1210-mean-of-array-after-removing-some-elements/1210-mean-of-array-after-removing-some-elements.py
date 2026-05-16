class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        n = len(arr)
        remove = int(n * 0.05)

        # while remove > 0:
        #     arr.pop(-1)
        #     del arr[0]
            
        #     remove -= 1
        arr = arr[remove: n - remove ]
        
        if len(arr) == 0:
            return 0
        
        return sum(arr) / len(arr)

