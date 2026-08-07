import bisect

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        
        
        for x in arr1:
            i = bisect.bisect_left(arr2, x)
            
            valid = True
            
            if i < len(arr2) and abs(arr2[i] - x) <= d:
                valid = False
            
            if i > 0 and abs(arr2[i-1] - x) <= d:
                valid = False
            
            if valid:
                count += 1
                
        return count