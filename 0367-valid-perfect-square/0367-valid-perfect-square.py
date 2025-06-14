class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left = 1
        right = num //2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1
            else:
                right = mid -1    

        return False
