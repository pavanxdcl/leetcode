class Solution:
    def trap(self, height: List[int]) -> int:
        m1=[0]*len(height)
        m2=[0]*len(height)

        m1[0]=height[0]
        for i in range(1,len(m1)):
            m1[i]=max(m1[i-1],height[i])
        
        m2[-1]=height[-1]
        for i in range(len(m2)-2,-1,-1):
            m2[i]=max(m2[i+1],height[i])
        
        sum=0
        for i in range(1,len(m2)-1):
            if(min(m1[i-1],m2[i+1])-height[i]>0):
                sum=sum+min(m1[i-1],m2[i+1])-height[i]
        return sum
        