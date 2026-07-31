class Solution:
    def maxDepth(self, s: str) -> int:
        a=[]
        m=0
        count=0
        for i in s:
            if(i=='('):
                a.append(i)
                count=count+1
                m=max(m,count)
            elif i==')':
                count=count-1 
                a.pop()

        return m