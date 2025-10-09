class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums_str = list(map(str , nums))

        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1  
            else:
                return 0
        nums_str.sort(key=cmp_to_key(cmp))
        ans = "".join(nums_str)


        return "0" if ans[0] == "0" else ans