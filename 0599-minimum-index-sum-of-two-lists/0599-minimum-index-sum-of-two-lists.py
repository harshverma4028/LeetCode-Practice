class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {name: i for i,name in enumerate(list1) }
        min_sum = float('inf')
        result = []

        for j, name in enumerate(list2):
            if name in index_map:
                i = index_map[name]
                index_sum = i + j
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [name]
                elif index_sum == min_sum:
                    result.append(name)
        return result