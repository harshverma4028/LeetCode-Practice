class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        covered = [False] * 51

        for l,r in ranges:
            for i in range(l,r+1):
                covered[i] = True
            
        
        for i in range(left,right+1):
            if not covered[i]:
                return False
        
        return True
        