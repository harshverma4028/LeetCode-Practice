class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
                # Memory optimized way
        prev = None
        for row in matrix:
            if prev:
                if row[1:] != prev[:-1]:
                    return False
            prev = row

        return True
        
        # for i in range(len(matrix)-1):
        #     for j in range(len(matrix[0])-1):
        #         if matrix[i][j] != matrix[i+1][j+1]:
        #             return False
        
        # return True