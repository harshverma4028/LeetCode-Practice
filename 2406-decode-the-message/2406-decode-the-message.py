class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        current_char = 'a'
        
        # build
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = current_char
                current_char = chr(ord(current_char) + 1)
        
        # decode
        decoded = []
        for ch in message:
            if ch == ' ':
                decoded.append(' ')
            else:
                decoded.append(mapping[ch])
        
        return ''.join(decoded)