class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) not in s:
                return False
        
        return True
            