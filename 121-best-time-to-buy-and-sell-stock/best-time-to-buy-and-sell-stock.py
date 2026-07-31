class Solution:
    def maxProfit(self, p: List[int]) -> int:
        minn=[0]*len(p)
        maxx=[0]*len(p)

        minn[0]=p[0]
        for i in range(1,len(p)):
            minn[i]=min(minn[i-1],p[i])

        maxx[-1]=p[-1]

        i=len(p)-2
        while(i>=0):
            maxx[i]=max(maxx[i+1],p[i])
            i=i-1
        
        ans=0
        for i in range(1,len(p)-1+1):
            ans=max(ans,maxx[i]-minn[i-1])
        return ans
        