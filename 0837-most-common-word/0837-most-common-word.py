from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())

        banned_set = set(banned)

        counts = Counter(word for word in words if word not in banned_set)

        return counts.most_common(1)[0][0]
