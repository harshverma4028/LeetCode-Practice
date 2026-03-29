class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        n = len(sequence)
        m = len(word)

        for i in range(n):
            current_consecutive = 0
            temp_i = i
            
            while sequence[temp_i : temp_i + m] == word:
                current_consecutive += 1
                temp_i += m  
            
            if current_consecutive > ans:
                ans = current_consecutive
        return ans