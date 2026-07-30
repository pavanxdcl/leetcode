class Solution:
    def twoSum(self, a: List[int], x: int) -> List[int]:
        i=0
        j=len(a)-1
        p=[]
        while i<j:
            if(a[i]+a[j]==x):
                p=[]
                p.append(i+1)
                p.append(j+1)
                return p
            elif(a[i]+a[j]<x):
                i=i+1
            else:
                j=j-1
        return p