class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        res = 0
        n = len(mat)

        for i in range(len(mat)):
            res += mat[i][i]
            if i != n-1-i:
                res += mat[i][n-1-i]

        return res