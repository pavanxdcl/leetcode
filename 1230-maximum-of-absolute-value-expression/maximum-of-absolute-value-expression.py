class Solution:
    def maxAbsValExpr(self, a: List[int], b: List[int]) -> int:
        a1=[]
        b1=[]
        c1=[]
        d1=[]

        for i in range(len(a)):
            a1.append(a[i]+b[i]+i)
            b1.append(a[i]+b[i]-i)
            c1.append(a[i]-b[i]+i)
            d1.append(a[i]-b[i]-i)
        
        a=max(a1)-min(a1)
        b=max(b1)-min(b1)
        c=max(c1)-min(c1)
        d=max(d1)-min(d1)

        return max(max(a,b),max(c,d))
        