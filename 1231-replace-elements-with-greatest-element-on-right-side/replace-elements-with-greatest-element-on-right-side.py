class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        maxx=[0]*len(a)
        maxx[-1]=a[-1]
        i=len(a)-2
        while(i>=0):
            maxx[i]=max(maxx[i+1],a[i])
            i=i-1
        
        if len(a)==1:
            return [-1]
        
        for i in range(0,len(a)-1):
            a[i]=maxx[i+1]
        a[-1]=-1
        return a