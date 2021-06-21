class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res=[]
        ans=""
        alphabet=[".-","-...","-.-.","-..",".",
                  "..-.","--.","....","..",".---",
                  "-.-",".-..","--","-.","---",".--.",
                  "--.-",".-.","...","-","..-","...-",
                  ".--","-..-","-.--","--.."]
        for i in words:
            for j in i:
                ans=ans+alphabet[ord(j)-97]
            res.append(ans)
            ans=""
        return len(set(res))
