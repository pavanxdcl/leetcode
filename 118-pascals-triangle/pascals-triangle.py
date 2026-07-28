class Solution:
    def fact(self,n):
        f=1
        for i in range(1,n+1,1):
            f=f*i
        return f
    def ncr(self,n,r):
        return self.fact(n)//(self.fact(n-r)*self.fact(r))

    def generate(self, a: int) -> List[List[int]]:
        aa=[]
        for i in range(0,a,1):
            x=[]
            for j in range(0,i+1,1):
                x.append(self.ncr(i,j))
            aa.append(x)
        return aa