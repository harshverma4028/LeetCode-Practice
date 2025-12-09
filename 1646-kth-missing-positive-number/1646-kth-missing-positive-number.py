class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = []
        s = set(arr)
        mis_c = 0
        for i in range(1,len(arr)+k+1):
            if i not in s:
                mis_c += 1
                if mis_c == k:
                    return i