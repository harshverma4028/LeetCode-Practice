class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_diff = 0

        for i in range(1,len(points)):
            x1,y1 = points[i-1]
            x2,y2 = points[i]

            total_diff += max(abs(x2-x1),abs(y2-y1))

        return total_diff