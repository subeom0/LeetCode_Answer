class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = -sys.maxsize
        _sum = 0
        
        for i in range(len(nums)):
            if _sum<0:
                _sum = nums[i]
            else:
                _sum += nums[i]
            _max = max(_max, _sum)
        
        return _max
