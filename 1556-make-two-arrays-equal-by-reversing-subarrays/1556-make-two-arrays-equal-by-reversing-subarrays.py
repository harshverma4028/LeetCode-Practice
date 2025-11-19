from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrd = {}
        arrt = {}
        for i in range(len(arr)):
            if arr[i] in arrd:
                arrd[arr[i]] += 1
            else:
                arrd[arr[i]] = 1
        for j in range(len(target)):
            if target[j] in arrt:
                arrt[target[j]] += 1
            else:
                arrt[target[j]] = 1
        
        if arrt == arrd:
            return True 
        else:
            return False


        # arrs = Counter(arr)
        # tar = Counter(target)
        # if arrs != tar:
        #     return False
        # else:
        #     return True
