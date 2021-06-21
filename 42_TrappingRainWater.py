class Solution:
    def trap(self, height: List[int]) -> int:
#         주어진 list의 길이가 0을 포함하기 때문에 길이가 0일 경우 0을 반환하도록 설계
        if len(height)==0:
            return 0
        
        ans = 0
        
        left=0; right=len(height)-1
        l_max=height[left]; r_max=height[right]
        while(left<right):
            
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            
            if l_max <= r_max:
                ans += l_max - height[left]
                left+=1
            else:
                ans += r_max - height[right]
                right-=1
        return ans
