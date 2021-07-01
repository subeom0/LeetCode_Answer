class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        _list = list(s)
        stack = []
        
        for i in range(len(_list)):
            if _list[i]=='(':
                stack.append(i)
            elif _list[i]==')':
                if stack:
                    stack.pop()
                else:
                    _list[i]=''
        
        if stack:
            for i in stack:
                _list[i]='0'
        
        return re.sub('[0]','',''.join(_list))
