class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citya = set()
        for i in range(len(paths)):
            citya.add(paths[i][0])
        
        for i in range(len(paths)):
            if paths[i][1] not in citya:
                return paths[i][1]