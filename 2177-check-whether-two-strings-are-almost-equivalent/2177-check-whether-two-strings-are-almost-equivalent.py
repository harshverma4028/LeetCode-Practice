class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 =  {}
        freq2 = {}

        for i in range(len(word1)):
            if word1[i] not in freq1:
                freq1[word1[i]] = 1
            else:
                freq1[word1[i]] += 1

        for i in range(len(word2)):
            if word2[i] not in freq2:
                freq2[word2[i]] = 1
            else:
                freq2[word2[i]] += 1
        
        
        for ch in freq1:
            if ch in freq2:
                if abs(freq1[ch] - freq2[ch])  > 3 :
                    return False
            else:
                if freq1[ch] > 3:
                    return False
                
        for ch in freq2:
            if ch in freq1:
                if abs(freq1[ch]- freq2[ch])  > 3 :
                    return False
            
            else:
                if freq2[ch] > 3:
                    return False
        
        return True

