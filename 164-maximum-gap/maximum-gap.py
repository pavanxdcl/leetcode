class Solution:
    def maximumGap(self, a: List[int]) -> int:
        a.sort()
        m=0
        for i in range(1,len(a)):
            m=max((a[i]-a[i-1]),m)
        return m