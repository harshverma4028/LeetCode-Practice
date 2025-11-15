class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            sol = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    sol += 1    
            res.append([sol,i])
        
        res.sort()
        val = []
        for i in range(k):
            val.append(res[i][1])


        return val