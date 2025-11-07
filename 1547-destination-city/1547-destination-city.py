class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citya = set()
        for i in range(len(paths)):
            for j in range(2):
                if j == 0:
                    citya.add(paths[i][j])
        
        for i in range(len(paths)):
            for j in range(2):
                if j == 1:
                    if paths[i][j] not in citya:
                        return paths[i][j]