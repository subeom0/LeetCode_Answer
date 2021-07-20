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

# itertools 함수에서 (중복)순열, (중복)조합을 함수로 사용할 수 있습니다.

# itertools.permutations(List, m) -> 순열(nPm)
# itertools.permutations(List, m) -> 중복순열(nPIm)
# itertools.combinations(List, m) -> 조합(nCm)
# itertools.combinations_with_replacement(List, m) -> 중복조합(nHm)
