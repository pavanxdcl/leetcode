class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        x=nums+nums[::-1]
        return x
        