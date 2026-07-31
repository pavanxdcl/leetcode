class Solution:
    def pivotIndex(self, a: List[int]) -> int:
        left=[0]*len(a)
        right=[0]*len(a)
        
        left[0]=a[0]
        right[-1]=a[-1]
        if len(a)==1:
            return 0
        i=1
        j=len(a)-2
        
        while(i<=len(a)-1):
            left[i]=left[i-1]+a[i]
            right[j]=right[j+1]+a[j]
            i=i+1
            j=j-1
        
        # print(a)
        # print(left)
        # print(right)

        if(right[1]==0):
            return 0
        for i in range(1,len(a)-1,1):
            # print(left[i],right[i+1])
            if(left[i-1]==right[i+1]):
                return i
        if(left[-2]==0):
            return len(a)-1
        return -1
        