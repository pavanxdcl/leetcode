class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if(nums[0]+nums[1]<=nums[2]):
            return "none"
    
        if(nums[0]+nums[2]<=nums[1]):
            return "none"
        
        if(nums[1]+nums[2]<=nums[0]):
            return "none"

        
        n=set(nums)
        if len(n)==1:
            return "equilateral"
        elif len(n)==2:
            return "isosceles"
        else:
            return "scalene"
