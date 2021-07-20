#다익스트라 알고리즘 사용 - 시간초과 오답

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for b, e, p in flights:
            graph[b].append((e, p))
        
        Q = [(0, src, k+1)]
        
        while Q:
            price, node, tmp = heapq.heappop(Q)
            if node == dst:
                return price
            
            if tmp>0:
                for e, p in graph[node]:
                    alt = price + p
                    heapq.heappush(Q, (alt, e, tmp-1))
        
        return -1
