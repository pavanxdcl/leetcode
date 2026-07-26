class Solution:
    def longestPalindrome(self, a: str) -> str:
        ans=""
        for i in range(len(a)):
            for j in range(i,len(a)):
                if(a[i]==a[j]):
                    curr=a[i:j+1]
                    if(curr==curr[::-1]):
                        if(len(ans)<len(curr)):
                            ans=curr
        return ans
        