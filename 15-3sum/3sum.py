class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=list()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    x=[]
                    x.append(nums[i])
                    x.append(nums[j])
                    x.append(nums[k])
                    ans.append(x)
                    j=j+1
                    k=k-1
                elif(nums[i]+nums[j]+nums[k]>0):
                    k=k-1
                else:
                    j=j+1
        x=[]
        s=set()
        for i in ans:
            find=str(i)
            if find not in s:
                s.add(find)
                x.append(i)
        return x
        