class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        m_dur = 0
        res = ""
        prev_time = 0

        for i in range(len(releaseTimes)):
            cur = releaseTimes[i] - prev_time

            if m_dur < cur:
                m_dur = cur
                res = keysPressed[i]
            
            elif cur == m_dur and keysPressed[i] > res:
                res = keysPressed[i]
                
            prev_time = releaseTimes[i]
    
        return res
