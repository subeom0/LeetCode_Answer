class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(comb, s: int, k: int):
            if k == 0:
                res.append(comb[:])
                return
            
            for i in range(s, n+1):
                comb.append(i)
                dfs(comb, i+1, k-1)
                comb.pop()
        
        dfs([], 1, k)
        return res
    
        # i = list(range(1, n+1))
        # return itertools.combinations(i, k)
