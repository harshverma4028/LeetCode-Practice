class Solution:
    def minTimeToType(self, word: str) -> int:
        dis = 0
        current = 'a'

        for i in range(len(word)):
            target = word[i]
            normal_dis = abs(ord(current) - ord(target))
            cir_dis = 26 - normal_dis
            dis += min(cir_dis,normal_dis) + 1
            current = target

        return dis