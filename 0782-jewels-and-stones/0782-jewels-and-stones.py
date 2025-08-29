class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewl_set = set(jewels)

        for stone in stones:
            if stone in jewl_set:
                count += 1

        return count
            