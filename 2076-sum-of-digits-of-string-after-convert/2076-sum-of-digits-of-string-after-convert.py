class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""

        for ch in s:
            inte = ord(ch) - ord('a') + 1
            res += str(inte)

        
        for _ in range(k):
            temp = 0
            for ch in res:
                temp += int(ch)
            res = str(temp)


        return int(res)