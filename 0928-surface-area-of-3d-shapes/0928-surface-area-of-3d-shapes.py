class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]

                if h > 0:
                    total +=  6 * h

                    total -= 2 *( h -1 )

                    if i > 0:
                        total  -= 2 * min(h , grid[i-1][j])
                    
                    if j > 0:
                        total -= 2 * min(h, grid[i][j - 1])

        return total