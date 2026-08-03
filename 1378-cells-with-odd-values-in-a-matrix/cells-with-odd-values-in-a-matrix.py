class Solution:
    def oddCells(self, m: int, n: int, x: List[List[int]]) -> int:
        a=[[0 for i in range(n)] for i in range(m)]
        count=0
        for k in x:
            for i in range(n):
                a[k[0]][i]=a[k[0]][i]+1
            for i in range(m):
                a[i][k[1]]=a[i][k[1]]+1
        # print(a)
        for i in a:
            for j in i:
                if j%2==1:
                    count=count+1

        return count