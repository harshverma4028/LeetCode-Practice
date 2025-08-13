class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start , target , path):
            if target == 0:
                result.append(list(path))
            
            if target < 0:
                return

            for i in range(start , len(candidates)):
                path.append(candidates[i])
                backtrack(i , target - candidates[i] , path)
                path.pop()
        
        backtrack(0 , target , [])
        return result
        