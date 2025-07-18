# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n

        left , right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid -1
            else:
                left = mid + 1 
