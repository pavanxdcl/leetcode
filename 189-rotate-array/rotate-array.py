class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        x=nums[len(nums)-k:]+nums[0:len(nums)-k]
        i=0
        for j in x:
            nums[i]=j
            i=i+1