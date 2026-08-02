class Solution:
    def fourSum(self, a: List[int], xt: int) -> List[List[int]]:
        a.sort()
        s=set()
        ans=[]

        for i in range(0,len(a)-1+1,1):
            for j in range(i+1,len(a)-1+1,1):
                k=j+1
                l=len(a)-1
                while(k<l):
                    if(a[i]+a[j]+a[k]+a[l]==xt):
                        x=[]
                        x.append(a[i])
                        x.append(a[j])
                        x.append(a[k])
                        x.append(a[l])
                        if(str(x) not in s):
                            s.add(str(x))
                            ans.append(x)
                        k=k+1
                        l=l-1
                    elif((a[i]+a[j]+a[k]+a[l])>xt):
                        l=l-1
                    else:
                        k=k+1
        return ans