class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openToclose = {")":"(","}":"{","]":'['}

        for c in s:
            if c in openToclose:
                if stack and stack[-1] == openToclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                
                