class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = collections.defaultdict(list)
        
        for b, e in prerequisites:
            dic[b].append(e)
        
        tmp, gone = set(), set()
        
        def dfs(i):
            if i in tmp:
                return False
            if i in gone:
                return True
            
            tmp.add(i)
            for e in dic[i]:
                if not dfs(e):
                    return False
            tmp.remove(i)
            gone.add(i)
            
            return True
        
        for x in list(dic):
            if not dfs(x):
                return False
            
        return True
