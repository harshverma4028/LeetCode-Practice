import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x in grid:
            arr.extend(x)
        k = k % len(arr)

        arr = arr[-k:] + arr[:-k]
        np_array = np.array(arr)




        return np_array.reshape(len(grid),len(grid[0])).tolist()
