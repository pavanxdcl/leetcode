class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        sum=0
        for i in range(len(a)):
            for j in range(len(a)):
                if(i==j):
                    sum=sum+a[i][j]
        sum2=0
        for i in range(len(a)):
            for j in range(len(a)):
                if(i+j==len(a)-1):
                    sum2=sum2+a[i][j]
        if(len(a)%2==1):
            sum=sum-a[(len(a)//2)][(len(a)//2)]
        return sum+sum2