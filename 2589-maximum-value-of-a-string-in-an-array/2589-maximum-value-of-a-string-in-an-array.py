class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # bada = 0

        # for word in strs:
        #     if word.isnumeric():
        #         if int(word) > bada:
        #             bada = int(word)
        #     else:
        #         if len(word) > bada:
        #             bada = len(word)
        
        # return bada


        return max(int(s) if s.isdigit() else len(s) for s in strs)
