class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        
        for i in range(len(arr)):
            if arr[i] not in freq:
                freq[arr[i]] = 1
            
            else:
                freq[arr[i]] += 1

        flag = 0
        for key,value in freq.items():
            if value == 1:
                flag += 1
            
                if flag == k:
                    return key

        return ""