class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])

        res = [[0] * n for _ in range(m)]

        def smooth(i , j ):
            total = 0
            count = 0 

            for dx in [-1, 0 ,1]:
                for dy in [-1 , 0 , 1]:
                    x_new = i + dx
                    y_new = j + dy 

                    if 0 <= x_new < m and 0 <= y_new < n:
                        total += img[x_new][y_new]
                        count += 1
                    
            return total // count

        for i in range(m):
            for j in range(n):
                res[i][j] = smooth(i, j)
        return res
