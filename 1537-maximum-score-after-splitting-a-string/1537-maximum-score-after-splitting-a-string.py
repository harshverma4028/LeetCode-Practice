class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        total_ones = s.count("1")
        left_zeros = 0
        right_ones = total_ones
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            score = max(score, left_zeros + right_ones)

        return score