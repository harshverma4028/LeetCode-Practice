class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        i = 0
        j = cols -1
        count = 0
        while i < rows and j >= 0:
            if grid[i][j] < 0:
                count = count + ( rows - i )
                j -= 1
            else:
                i += 1

        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] < 0:
        #             count += 1
        
        return count