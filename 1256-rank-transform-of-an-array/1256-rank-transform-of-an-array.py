class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(list(set(arr)))

        rank_map = {}
        for i in range(len(unique_sorted)):
            rank_map[unique_sorted[i]] = i + 1
        
        res = []
        for x in arr:
            res.append(rank_map[x])


        return res

        