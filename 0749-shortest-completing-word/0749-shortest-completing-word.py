from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        target = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        result = None  

        for word in words:
            word_count = Counter(word.lower())
            ok = True  

            for c in target:
                if word_count[c] < target[c]: 
                    ok = False
                    break

            if ok:
                if result is None or len(word) < len(result):
                    result = word 

        return result
