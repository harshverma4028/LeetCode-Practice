class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."] 

        unique_set = set()

        for word in words:
            code = []

            for ch in word:
                index = ord(ch) - ord('a')
                code.append(morse[index])
            unique_set.add("".join(code))
        
        return len(unique_set)