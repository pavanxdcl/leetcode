class Solution:
    def heightChecker(self, h: List[int]) -> int:
        nums=[]
        for i in h:
            nums.append(i)
        h.sort()
        count=0
        j=0
        for i in nums:
            if i!=h[j]:
                count=count+1
            j=j+1
        return count

        