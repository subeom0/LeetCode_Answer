class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        
        for b, e in sorted(tickets):
            dic[b].append(e)

        res = []
        
        def dfs(s):
            while dic[s]:
                dfs(dic[s].pop(0))
            res.append(s)
        
        dfs('JFK')
        return res[::-1]
