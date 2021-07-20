class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []
        
        def dfs(perm):
            if len(perm) == 0:
                res.append(prev[:])
                
            for i in perm:
                tmp = perm[:]
                tmp.remove(i)
                
                part.append(i)
                dfs(tmp)
                part.pop()
                
        dfs(nums)
        return res
