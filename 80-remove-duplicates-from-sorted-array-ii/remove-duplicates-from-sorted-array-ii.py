class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        h={}
        for i in a:
            if(i in h.keys()):
                h[i]=h[i]+1
            else:
                h[i]=1
        
        l=list(h.keys())
        l.sort()
        x=0
        for i in l:
            if h[i]==1:
                a[x]=i
                x=x+1
            else:
                a[x]=i
                x=x+1
                a[x]=i
                x=x+1
        return x
        