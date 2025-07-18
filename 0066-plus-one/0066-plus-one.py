class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] = digits[i]+1
                return digits

            if digits[i] == 9:
                digits[i] = 0

        return [1] + digits   