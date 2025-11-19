from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if set(target) != set(arr):
            return False
        
        else:
            arrs = Counter(arr)
            tar = Counter(target)
            if arrs != tar:
                return False
            else:
                return True
