class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        t=set()
        m=0
        for i in a:
            if i-1 not in t:
                count=1
                while(i+1 in a):
                    t.add(i+1)
                    count=count+1
                    i=i+1
            m=max(m,count)
        return m