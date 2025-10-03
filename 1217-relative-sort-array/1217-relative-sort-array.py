class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
                
        res = []
        for num in arr2:
            for x in arr1:
                if x == num:
                    res.append(x)
        
        rem = []
        for x in arr1:
            if x not in arr2:
                rem.append(x)

        rem.sort()
        res.extend(rem)
        return res
