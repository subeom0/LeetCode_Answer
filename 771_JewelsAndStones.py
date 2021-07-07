class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # 한줄코드
        # return sum(s in jewels for s in stones)
        
        freq = {}
        cnt = 0
        
        for i in stones:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for i in jewels:
            if i in freq:
                cnt += freq[i]
        
        return cnt
