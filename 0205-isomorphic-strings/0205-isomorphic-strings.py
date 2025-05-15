class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}    

        for ch_s , ch_t in zip( s, t ):
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False

            if ch_t in t_to_s:
                if t_to_s[ch_t] != ch_s:
                    return False

            s_to_t[ch_s] = ch_t
            t_to_s[ch_t] = ch_s                
        return True    