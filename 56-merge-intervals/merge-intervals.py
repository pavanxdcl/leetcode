class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        print(a)
        curr=a[0]
        start=curr[0]
        end=curr[1]
        ans=[]
        mark=0
        pure=0
        for i in range(1,len(a)-1+1,1):
            mark=0
            if(a[i][0]<=end):
                end=max(end,a[i][1])
                mark=2
                pure=1
            else:
                temp=[]
                temp.append(start)
                temp.append(end)
                ans.append(temp)
                mark=1
                start=a[i][0]
                end=a[i][1]
                pure=1

        if(mark==1 or mark==2 or pure==0):
            temp=[]
            temp.append(start)
            temp.append(end)
            ans.append(temp)

        return ans
