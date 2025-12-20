class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique_numbers = set()
        current = ""

        for ch in word:
            if ch.isdigit():
                current += ch
            
            else:
                if current:
                    current = current.lstrip('0')
                    if current == "":
                        current = "0"
                    unique_numbers.add(current)
                    current = ""
                
        if current:
            current = current.lstrip('0')
            if current == "":
                current = "0"
            unique_numbers.add(current)
    
        return len(unique_numbers)
        
