class Solution:
    def minMoves(self, a: List[int]) -> int:
        m=max(a)
        sum=0
        for i in a:
            sum=sum+(m-i)
        return sum