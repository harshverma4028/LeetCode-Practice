from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck).values()
        g = reduce(math.gcd, freq)
        return g >= 2



