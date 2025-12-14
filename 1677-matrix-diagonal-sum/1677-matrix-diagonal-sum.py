class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(
            mat[i][i] + (mat[i][n-1-i] if i != n-1-i else 0)
            for i in range(n)
        )

        # res = 0
        # n = len(mat)

        # for i in range(len(mat)):
        #     res += mat[i][i]
        #     if i != n-1-i:
        #         res += mat[i][n-1-i]

        # return res