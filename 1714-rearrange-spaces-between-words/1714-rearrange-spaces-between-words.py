class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = text.split()
        

        if len(words) == 1:
            return words[0] + " " * spaces


        gaps = len(words) - 1


        e_spaces = spaces // gaps
        ex_spaces = spaces % gaps


        return (" " * e_spaces).join(words) + " " * ex_spaces