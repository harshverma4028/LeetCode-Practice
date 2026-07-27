class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        up = low = sp = digit  = False 
        special = set("!@#$%^&*()-+")

        if len(password) < 8:
            return False
        
        for i in range(len(password)):
            if i > 0 and password[i] == password[i-1]:
                return False

            if password[i] in special:
                sp = True
            
            elif password[i].isupper():
                up = True

            elif password[i].islower():
                low = True
            
            elif password[i].isdigit():
                digit = True

        if up and low and sp and digit:
            return True

        return False