class Solution:
    def maximumDifference(self, a: List[int]) -> int:
        minn=a[0]
        best=-1
        for i in a:
            if i>minn:
                best=max(best, (i-minn))
            if minn>i:
                minn=i
                # best=max(best,i-minn)
        
        return best
            