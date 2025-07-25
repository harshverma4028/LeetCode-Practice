class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        i = 0
        for word in word_list:
            word = list(word)
            left, right = 0, len(word)-1
            while left < right:
                word[left] , word[right] = word[right] , word[left]
                left += 1
                right -= 1
            word_list[i] = "".join(word) 
            i +=1   

        return ' '.join(word_list)        