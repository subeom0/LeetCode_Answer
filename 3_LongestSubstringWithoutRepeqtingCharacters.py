class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt, _max = '', 0
        
        for i in s:
            if i in cnt:
                _max = max(len(cnt), _max)
                cnt = cnt[cnt.index(i)+1:] + i
            else:
                cnt += i
        
        _max = max(len(cnt), _max)
        
        return _max
