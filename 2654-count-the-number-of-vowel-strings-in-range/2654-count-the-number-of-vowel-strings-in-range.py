class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = set("aeiou")
        count = 0

        for i in range(left,right+1):
            n = len(words[i])-1
            if words[i][0] in vowel and words[i][n] in vowel:
                count += 1
            
        return count