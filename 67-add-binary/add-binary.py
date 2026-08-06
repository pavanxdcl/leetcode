class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        if(a=='0' and b=='0'):
            return "0"
        x=0
        ans=0
        for i in a:
            if i=='1':
                ans=ans+(2**int(x))
            x=x+1
        
        x=0
        ans1=0
        for i in b:
            if i=='1':
                ans1=ans1+(2**int(x))
            x=x+1
        
        ans=ans+ans1
        s=""
        while(ans!=0):
            s=str((ans%2))+s
            ans=ans//2
        return s