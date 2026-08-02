class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        sum=0
        while(n!=1):
            sum=0
            while(n!=0):
                sum=sum+((n%10)**2)
                n=n//10
            if sum in s:
                return False
            s.add(sum)
            n=sum
        
        return True
