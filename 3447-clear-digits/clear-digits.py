class Solution:
    def clearDigits(self, s: str) -> str:
        ss=[]
        for i in s:
            if(len(ss)!=0 and ord(i)>=48 and ord(i)<=57):
                ss.pop()
            else:
                ss.append(i)
        s=""
        for i in ss:
            s=s+i
        return s