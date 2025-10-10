from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_len = 0

        for word in words:
            word_count = Counter(word)
            good_word = True
            for char, required_count in word_count.items():
                if chars_count[char] < required_count:
                     good_word = False
                     break
                
            if good_word is True:
                total_len += len(word)
        
        return total_len
                
                