class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i in h.keys():
                h[i]=h[i]+1
                if h[i]==len(nums)//2:
                    return i
            else:
                h[i]=1
        