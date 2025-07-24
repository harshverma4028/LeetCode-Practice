class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_count = 0
        for char in s:
            if char == 'A':
                a_count += 1
                if a_count >= 2:
                    return False

            if char == "L":
                l_count += 1
                
            else:
                l_count = 0  

            if a_count >= 2 or l_count >= 3:
                return False

        return True            
                