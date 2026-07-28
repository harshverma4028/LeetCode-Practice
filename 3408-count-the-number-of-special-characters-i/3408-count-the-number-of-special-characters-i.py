class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        s = set()
        c = set()
        res = 0
        counted = set()

        for char in word:
            if char.islower():
                if char.upper() in c:
                    counted.add(char)

                else:
                    s.add(char)
            else:
                if char.lower() in s:
                    counted.add(char)
                else:
                    c.add(char)

        return len(counted)