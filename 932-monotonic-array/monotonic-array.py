class Solution:
    def isMonotonic(self, a: List[int]) -> bool:
        m1=True
        for i in range(1,len(a)-1+1,1):
            if(a[i-1]>a[i]):
                m1=False
        
        m2=True
        for i in range(1,len(a)-1+1,1):
            if(a[i-1]<a[i]):
                m2=False
        
        return (m1 or m2)