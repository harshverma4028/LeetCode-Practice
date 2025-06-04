class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for c,w in zip(pattern , words):
            if c in char_to_word:
                # checking for consistant
                if char_to_word[c] != w:
                    return False    
            else:
                char_to_word[c] = w


            if w in word_to_char:
                # check for consistent
                if word_to_char[w] != c:
                    return False

            else:
                word_to_char[w] = c   

        return True                 