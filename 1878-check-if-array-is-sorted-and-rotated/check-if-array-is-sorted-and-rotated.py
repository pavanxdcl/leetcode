class Solution:
    def check(self, a: List[int]) -> bool:
        i=0
        while(i<=len(a)-2 and a[i]<=a[i+1]):
            i=i+1
        
        if(i==len(a)-1):
            return True
        else:
            a=a[i+1:]+a[:i+1]
            i=0
            while(i<=len(a)-2 and a[i]<=a[i+1]):
                i=i+1
            if(i==len(a)-1):
                return True
        return False