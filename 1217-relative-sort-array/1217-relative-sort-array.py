from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        res = []
        freq = Counter(arr1)
        for x in arr2:
            res.extend([x] * freq[x])
            del freq[x]
        
        rem = []

        for num,count in freq.items():
            rem.extend([num] * count)

        res.extend(sorted(rem))

        return res



        # res = []
        # for num in arr2:
        #     for x in arr1:
        #         if x == num:
        #             res.append(x)
        
        # rem = []
        # for x in arr1:
        #     if x not in arr2:
        #         rem.append(x)

        # rem.sort()
        # res.extend(rem)
        # return res
