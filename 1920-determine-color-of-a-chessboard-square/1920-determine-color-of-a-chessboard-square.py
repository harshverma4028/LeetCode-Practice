class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a , b = coordinates[0], coordinates[1]

        return (((ord(a) - 96) + int(b)) % 2) == 1