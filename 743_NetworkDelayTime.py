class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for s, e, t in times:
            graph[s].append((e, t))
            
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for e, t in graph[node]:
                    alt = time + t
                    heapq.heappush(Q, (alt, e))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
