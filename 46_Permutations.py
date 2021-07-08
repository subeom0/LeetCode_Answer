class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []
        
        def dfs(num):
            if len(num) == 0:
                res.append(prev[:])
                
            for i in num:
                _next = num[:]
                _next.remove(i)
                
                prev.append(i)
                dfs(_next)
                prev.pop()
                
        dfs(nums)
        return res
