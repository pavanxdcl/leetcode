class Solution:
    def removeStars(self, x: str) -> str:
        s=[]
        for i in x:
            if i=='*':
                s.pop()
            else:
                s.append(i)
        
        ans=""
        for i in s:
            ans=ans+i
        return ans
        