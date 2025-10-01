class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        captures = 0

        for i in range(0,8):
            for j in range(0,8):
                if board[i][j] == 'R':
                    rook_row = i
                    rook_col = j
                    break

        directions = [(0,1), (0,-1), (1,0), (-1,0)]


        for dx, dy in directions:
            x, y = rook_row, rook_col
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                if board[x][y] == 'B':  
                    break
                if board[x][y] == 'p':  
                    captures += 1
                    break
        
        return captures        
