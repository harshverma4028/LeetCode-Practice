class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # hashs = set()

        # for i in range(len(height)-1):
        #     j = i + 1
        #     while j < len(height):
        #         water = min(height[i],height[j]) * (j -i )
        #         hashs.add(water)
        #         j += 1
        # return max(hashs)        

                
                # Optimal solution 
        left = 0
        right = len(height) - 1
        max_area = 0

        while left <= right:
            area = min(height[left],height[right]) * (right - left) 
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1     

        return max_area         