class Solution:
    def largestGoodInteger(self, num: str) -> str:
        same_digit_num = ["999","888","777","666","555","444","333","222","111","000"]

        for good_num in same_digit_num:
            if good_num in num:
                return good_num
        
        return ""