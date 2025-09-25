class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        galat = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                galat += 1
        
        
        return galat