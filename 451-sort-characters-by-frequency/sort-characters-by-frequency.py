class Solution:
    def frequencySort(self, s: str) -> str:
        h={}
        for i in s:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        x=list(set(h.values()))
        x.sort()
        i=len(x)-1
        ans=""
        while(i>=0):
            for j in range(65,91):
                if(j-17)<=58 and  chr(j-17) in s and h[chr(j-17)]==x[i]:
                    ans=ans+(chr(j-17)*x[i])
                if chr(j) in s and h[chr(j)]==x[i]:
                    ans=ans+(chr(j)*x[i])
                if chr(j+32) in s and h[chr(j+32)]==x[i]:
                    ans=ans+(chr(j+32)*x[i])
            i=i-1
        return ans