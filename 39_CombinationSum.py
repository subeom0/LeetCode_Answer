class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(comb, n, std):
            if std <0:
                return
            if std == 0:
                res.append(comb)
                return
            
            for i in range(n, len(candidates)):
                dfs(comb+[candidates[i]], i, std-candidates[i])
                
        dfs([], 0, target)
        return res
