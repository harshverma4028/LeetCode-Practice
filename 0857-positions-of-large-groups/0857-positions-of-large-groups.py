class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        for i in range(1,len(s)+1):
            if i == len(s) or s[i] != s[i-1]:
                
                group_length = i - start 
                if group_length >= 3:
                    res.append([start,i-1])

                start = i


        return res