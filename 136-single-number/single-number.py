class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set()
        sum=0

        for i in nums:
            if i in s:
                sum=sum-i
                s.remove(i)
            else:
                sum=sum+i
                s.add(i)
        return sum