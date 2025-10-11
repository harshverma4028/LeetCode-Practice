from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        text_list = list(text)
        count = 0
        
        while "b" in text_list and "a" in text_list and text_list.count("l") >= 2 and text_list.count("o") >= 2 and "n" in text_list:
            text_list.remove("b")
            text_list.remove("a")
            text_list.remove("l")
            text_list.remove("l")
            text_list.remove("o")
            text_list.remove("o")
            text_list.remove("n")

            count += 1


        return count