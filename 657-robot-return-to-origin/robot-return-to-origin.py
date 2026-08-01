class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,d,l,r=0,0,0,0
        for i in moves:
            if i=='U':
                u=u+1
            elif i=='D':
                d=d+1
            elif i=='L':
                l=l+1
            elif i=='R':
                r=r+1
            # print(i,c,end=" ")
        
        return (u-d==0 and r-l==0)
        