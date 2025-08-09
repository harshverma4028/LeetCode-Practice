class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        term = "1"
        for _ in range(n - 1 ):
            newterm = ''
            count = 1
            for i in range(1,len(term)+1):
                if i < len(term) and term[i] == term[i-1]:
                    count += 1
                else:
                    newterm += str(count) + term[i-1]
                    count = 1
            term = newterm
            
        return term