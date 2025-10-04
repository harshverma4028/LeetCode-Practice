from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        normalized = [(min(a, b), max(a, b)) for a, b in dominoes]
        
        freq = Counter(normalized)
        
        count = 0
        for val in freq.values():
            count += val * (val - 1) // 2
        
        return count

