class Solution:
    def isPalindrome(self, s: str) -> bool:
        sum=""
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                sum=sum+chr(ord(i)+32)
            elif ord(i)>=97 and ord(i)<=122:
                sum=sum+i
            elif ord(i)>=48 and ord(i)<=57:
                sum=sum+i
        # print(s)
        if sum==sum[::-1]:
            return True
        else:
            return False
        