class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        rowCount  = [0] * len(mat)
        colCount = [0] * len(mat[0])


        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    rowCount[i] = rowCount[i] + 1
                    colCount[j] = colCount[j] + 1
        
        special_count = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    special_count += 1



        return special_count
