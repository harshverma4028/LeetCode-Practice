class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cleaned = s.replace('-', '').upper()
    
    # Build result in reverse for ease of grouping
        result = []
        for i in range(len(cleaned)):
            if i > 0 and i % k == 0:
                result.append('-')
            result.append(cleaned[-(i+1)])
        
        # Reverse back and return
        return ''.join(reversed(result))