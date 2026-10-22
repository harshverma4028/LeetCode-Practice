class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        cols = len(matrix[0])

        for i in range(cols):
            m = float('-inf')
            for j in range(row):
                m = max(m,matrix[j][i])
            
            for j in range(row):
                if matrix[j][i] == -1:
                    matrix[j][i] = m
                
        return matrix
