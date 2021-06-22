class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        go=0
        if start<destination:
            for i in range(start, destination):
                go+=distance[i]
        else:
            for i in range(start-1, destination-1, -1):
                go+=distance[i]
        return min(go, sum(distance)-go)
