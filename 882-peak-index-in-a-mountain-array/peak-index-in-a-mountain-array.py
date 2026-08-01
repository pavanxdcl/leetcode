class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        i=0
        j=len(a)-1

        while(i<=j):
            mid=(i+j)//2
            if(a[mid-1]<a[mid] and a[mid]>a[mid+1]):
                return mid
            elif(a[mid-1]>a[mid] and a[mid]>a[mid+1]):
                j=mid-1
            else:
                i=mid+1
        