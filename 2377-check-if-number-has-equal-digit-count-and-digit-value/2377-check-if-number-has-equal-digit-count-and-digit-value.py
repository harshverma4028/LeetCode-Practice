class Solution:
    def digitCount(self, num: str) -> bool:
        
        freq = {}

        for ch in num:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(num)):
            if freq.get(str(i), 0) != int(num[i]):
                return False

        return True


        # for i in range(len(num)):
        #     if num.count(str(i)) != int(num[i]):
        #         return False
        # return True