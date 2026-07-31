class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        j=0
        for i in range(len(a)):
            if a[i]!=0:
                a[j],a[i]=a[i],a[j]
                j=j+1
        