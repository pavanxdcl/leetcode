class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        for i in s:
            if(len(s1)!=0 and i=='#'):
                s1.pop()
            elif(i!='#'):
                s1.append(i)
        
        s2=[]
        for i in t:
            if(len(s2)!=0 and i=='#'):
                s2.pop()
            elif(i!='#'):
                s2.append(i)
        return s1==s2