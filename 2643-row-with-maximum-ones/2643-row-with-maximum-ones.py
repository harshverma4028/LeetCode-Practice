class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        row_index = 0

        for i in range(len(mat)):
            curr_ones = 0

            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    curr_ones += 1

            if curr_ones > max_ones:
                max_ones = curr_ones
                row_index = i

        return [row_index, max_ones]