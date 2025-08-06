class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        # We make a copy to avoid modifying the original list passed to the function
        fbed = flowerbed[:] 
        length = len(fbed)

        for i in range(length):
            if fbed[i] == 0:
                is_left_empty = (i == 0) or (fbed[i-1] == 0)
                is_right_empty = (i == length - 1) or (fbed[i+1] == 0)

                if is_left_empty and is_right_empty:
                    fbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False