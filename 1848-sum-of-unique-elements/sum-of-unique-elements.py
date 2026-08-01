class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        
        ans=0
        for i in h.keys():
            if h[i]==1:
                ans=ans+i
        return ans
        