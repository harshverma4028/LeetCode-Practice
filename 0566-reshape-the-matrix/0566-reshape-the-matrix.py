class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        total = m * n

        if total != r * c:
            return mat
        
        flat = []
        for row in mat:
            flat.extend(row)

        reshaped = []
        index = 0
        for i in range(r):
            row = []
            
            for j in range(c):
                row.append(flat[index])
                index += 1
            reshaped.append(row)

        return reshaped
