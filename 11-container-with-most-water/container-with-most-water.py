class Solution:
    def maxArea(self, a: List[int]) -> int:
        i=0
        j=len(a)-1
        m=0
        while(i<j):
            curr=min(a[i],a[j])*(j-i)
            m=max(curr,m)
            if(a[i]<a[j]):
                i=i+1
            else:
                j=j-1
        
        return m