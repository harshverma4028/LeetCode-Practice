class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top , right = 0 , len(matrix[0]) -1 
        bottom , left = len(matrix) -1 , 0

        while top <= bottom and left <= right:
            
            # top wala
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1

            # right
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -=1

            #bottom 
            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -=  1
            
            # left
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1

        return res
