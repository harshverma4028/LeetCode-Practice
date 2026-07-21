class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        base = 1950
        size = 101  # 1950..2050

        diff = [0] * size


        # Mark changes
        for birth, death in logs:
            diff[birth - base] += 1
            diff[death - base] -= 1   # death is exclusive


        # Prefix sum + track max
        max_pop = 0
        curr = 0
        year = base


        for i in range(size):
            curr += diff[i]
            if curr > max_pop:
                max_pop = curr
                year = base + i   # smallest year auto-handled

        return year