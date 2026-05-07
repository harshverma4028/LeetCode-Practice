class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0 
        col = cols - 1

        while row < rows and col >= 0:

            value = matrix[row][col]

            if target == value:
                return True

            elif target < value:
                col -= 1
            else:
                row += 1

        return False

