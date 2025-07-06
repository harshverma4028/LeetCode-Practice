class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current_string):
            # Base case: if current string length == digits length, add to result
            if index == len(digits):
                result.append(current_string)
                return
            
            # Get the letters for the current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, current_string + letter)

        # Start from index 0 with an empty string
        backtrack(0, "")
        return result