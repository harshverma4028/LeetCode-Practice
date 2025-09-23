from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                
                if len(w1) > len(w2):
                    return False
        return True
