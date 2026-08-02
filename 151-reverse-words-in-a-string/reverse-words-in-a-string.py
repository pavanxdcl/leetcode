class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split(' ')
        print(s)
        i=0
        j=len(s)-1
        while(i<j):
            s[i],s[j]=s[j],s[i]
            i=i+1
            j=j-1
        print(s)
        w=""
        for i in s:
            if len(i)!=0:
                w=w+i+" "
        return w[:len(w)-1:]
        