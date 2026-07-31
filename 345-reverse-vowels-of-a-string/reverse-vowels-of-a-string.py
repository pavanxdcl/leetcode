class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        a=list(s)
        i=0
        j=len(s)-1

        while(i<j):
            while(a[i] not in v and i<j):
                i=i+1
            while(a[j] not in v and i<j):
                j=j-1
            if(i<j):
                a[i],a[j]=a[j],a[i]
                i=i+1
                j=j-1
        
        s=""
        for i in a:
            s=s+i
        return s
        