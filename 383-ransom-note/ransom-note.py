class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r=list(r)
        r.sort()
        x=""
        for i in r:
            x=x+i

        m=list(m)
        m.sort()
        y=""
        for i in m:
            y=y+i
        
        j=0
        for i in y:
            if x[j]==i:
                j=j+1
            if j==len(x):
                return True
        
        return j == len(x)
            