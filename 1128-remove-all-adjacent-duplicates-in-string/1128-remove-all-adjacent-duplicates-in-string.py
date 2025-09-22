class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


                # Time complexity 0(N square )
        # s = list(s)
        # i = 1
        # while i < len(s):
        #     if s[i] == s[i-1]:
        #         s.pop(i),s.pop(i-1)
        #         i = 1
        #     else:
        #         i += 1

        # return "".join(s)