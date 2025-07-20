class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # return word.isupper()
      
        if all('A' <= c <= 'Z' for c in word):
            return True

        if all('a' <= c <= 'z' for c in word):
            return True

        if 'A' <= word[0] <= 'Z' and all('a' <= c <= 'z' for c in word[1:]):
            return True 

        return False    