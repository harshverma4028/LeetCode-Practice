class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        balance = 0
        for ch in s:
            if ch == '(':
                if balance > 0:
                    res += ch
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    res +=ch
        

        
        return res