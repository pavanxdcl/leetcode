class Solution:
    def insert(self, a: List[List[int]], b: List[int]) -> List[List[int]]:
        a.append(b)
        a.sort()
        if(len(a)==1 or len(a)==0):
            return a
        start=a[0][0]
        end=a[0][1]
        ans=[]
        mark=0
        for i in range(1,len(a)):
            if(a[i][0]<=end):
                end=max(a[i][1],end)
                mark=1
            else:
                x=[]
                x.append(start)
                x.append(end)
                ans.append(x)
                start=a[i][0]
                end=a[i][1]
                mark=1
        if mark==1:
            x=[]
            x.append(start)
            x.append(end)
            ans.append(x)
        return ans