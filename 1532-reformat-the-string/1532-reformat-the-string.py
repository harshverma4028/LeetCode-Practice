class Solution:
    def reformat(self, s: str) -> str:
        letters,digit = [],[]

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digit.append(ch)

        if abs(len(letters) - len(digit)) > 1:
            return ""

        if len(digit) > len(letters):
            a , b = digit,letters
        else:
            a ,b = letters , digit

        i = j = 0
        res = []

        while i < len(a) or j < len(b):
            if i < len(a):
                res.append(a[i])
                i += 1
            if j < len(b):
                res.append(b[j])
                j += 1
            
        return "".join(res)