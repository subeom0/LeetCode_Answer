class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        _min = sys.maxsize
        
        for i in prices:
            _min = min(_min, i)
            profit = max(profit, i - _min)
            
        return profit
