class Solution:
    def isValid(self, a: str) -> bool:
        s=[]
        for i in a:
            if i=='(' or i=='[' or i=='{':
                s.append(i)
            elif len(s)==0:
                return False
            elif i==']' and s[-1]=='[':
                s.pop()
            elif i==')' and s[-1]=='(':
                s.pop()
            elif i=='}' and s[-1]=='{':
                s.pop()
            else:
                return False
        
        return len(s)==0