class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        current_width = 0

        for ch in s:
            width = widths[ord(ch) - ord('a')]

            if current_width + width <= 100:
                current_width += width
            else:
                line += 1
                current_width = width

        return [line,current_width]