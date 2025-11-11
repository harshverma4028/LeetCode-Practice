class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(x):
            count = 0
            while x > 0:
                if x % 2 == 1:
                    count += 1
                
                x = x // 2
            return count

        arr.sort(key = lambda x: (countBits(x), x))
        return arr
