class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        count=0
        v=['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in v and count<=(len(s)//2)-1:
                c=c+1
            elif i in v:
                c=c-1
            count=count+1
        return 0==c