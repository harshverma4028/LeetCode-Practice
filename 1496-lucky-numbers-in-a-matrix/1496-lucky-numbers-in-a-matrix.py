class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_min = []
        col_max = []

        for row in matrix:
            row_min.append(min(row))

        for j in range(len(matrix[0])):
            col_val = []
            for i in range(len(matrix)):
                col_val.append(matrix[i][j])
            
            col_max.append(max(col_val))
        
        for x in row_min:
            if x in col_max:
                res.append(x)
        
        return res