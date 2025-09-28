class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            pile = stones[-1] - stones[-2]

            stones.pop()
            stones.pop()

            if pile != 0:
                stones.append(pile)


        return stones[0] if stones else 0