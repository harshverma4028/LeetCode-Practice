class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) <3:
            return False

        has_vowel = False 
        has_constant = False

        vowels = set("aeiouAEIOU")

        for char in word:
            if char.isdigit():
                continue
            elif char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_constant = True
                
            else:
                return False

        return has_vowel and has_constant
            
        