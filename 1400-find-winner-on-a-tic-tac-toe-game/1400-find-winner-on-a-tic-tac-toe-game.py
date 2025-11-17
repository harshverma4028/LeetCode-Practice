from typing import List , Set
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A_moves: Set[tuple] = set()
        B_moves: Set[tuple] = set()
        for i in range(len(moves)):
            my_tuple = tuple(moves[i])
            if i % 2  == 0:
                A_moves.add(my_tuple)
            else:
                B_moves.add(my_tuple)



        winning_patterns = [
        {(0,0), (0,1), (0,2)},   
        {(1,0), (1,1), (1,2)},    
        {(2,0), (2,1), (2,2)},    

        {(0,0), (1,0), (2,0)},    
        {(0,1), (1,1), (2,1)},   
        {(0,2), (1,2), (2,2)},    

        {(0,0), (1,1), (2,2)},    
        {(0,2), (1,1), (2,0)}     
        ]



        for pattern in winning_patterns:
            if pattern.issubset(A_moves):
                return "A"
            
            if pattern.issubset(B_moves):
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

