class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        mp = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        idx = mp[ruleKey]
        count = 0
        
        for item in items:
            if item[idx] == ruleValue:
                count += 1
                
        return count