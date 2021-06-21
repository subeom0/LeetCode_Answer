class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = len(nums)
        for i in range(t):
            for j in range(i+1,t):
                if nums[i]+nums[j]==target:
                    return [i, j]
