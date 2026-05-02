
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frq = {}

        for x in arr:
            if x not in frq:
                frq[x] = 1
            else:
                frq[x] += 1
                  
        s = set()
        for count in frq.values():
            if count not in s:
                s.add(count)
            else:
                return False
        return True