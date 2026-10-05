class Solution:
    def scoreBalance(self, s: str) -> bool:
        # n = len(s)
        # first = s[:n//2]
        # second = s[n//2 + n%2:]

        # return sum(ord(char) for char in first) == sum(ord(char) for char in second)

        total_sum = sum(ord(char) - ord('a') + 1 for char in s)

        left_sum = 0

        for i in range(len(s) - 1):
            left_sum += ord(s[i]) - ord('a') + 1
            
            if left_sum == total_sum - left_sum:
                return True

        return False