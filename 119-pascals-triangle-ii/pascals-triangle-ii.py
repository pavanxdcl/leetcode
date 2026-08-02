class Solution:
    def getRow(self, n: int) -> List[int]:
        n=n+1

        ans=1
        a=[]
        a.append(1)
        for i in range(1,n,1):
            ans=ans*(n-i)
            ans=ans//i
            a.append(ans)
        
        return a
        
        