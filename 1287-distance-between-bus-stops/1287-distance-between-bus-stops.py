class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        clock = 0
        i = start

        while i != destination:
            clock += distance[i]
            i = (i + 1) % len(distance)
        
        return min(clock , sum(distance) - clock)
