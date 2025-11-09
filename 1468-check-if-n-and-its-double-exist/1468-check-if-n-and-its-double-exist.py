class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        seen = set()
        for x in arr:
            
            if x * 2 in seen or x/2 in seen:
                return True
                
            seen.add(x)
        
        return False



        # p = 0
        # while p <= len(arr)-1:
        #     for i in range(p+1,len(arr)):
        #         if arr[p] == 2 * arr[i] or arr[i] == 2 * arr[p]:
        #             return True
        #     p += 1

        # return False