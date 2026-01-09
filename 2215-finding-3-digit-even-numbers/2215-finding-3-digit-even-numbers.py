class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        res = []

        for num in range(100, 1000, 2):  
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = [0] * 10
            need[a] += 1
            need[b] += 1
            need[c] += 1

            valid = True
            for d in range(10):
                if need[d] > freq[d]:
                    valid = False
                    break

            if valid:
                res.append(num)

        return res


        # res = set()

        # for i in range(len(digits)):
        #     if digits[i] == 0:
        #         continue
        #     for j in range(len(digits)):
        #         if i == j:
        #             continue
        #         for k in range(len(digits)):
        #             if i == k or j == k or digits[k] % 2 != 0:
        #                 continue
                    
        #             num = digits[i]*100 + digits[j]*10 + digits[k]
        #             res.add(num)

        # return sorted(list(res))