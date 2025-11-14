from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maps = {}

        for i in range(len(arr)):
            if arr[i] not in maps:
                maps[arr[i]] = 1
            else:
                maps[arr[i]] += 1

        res = -1
        for key,value in maps.items():
            if key == value:
                res = max(res, key)
        
        return res