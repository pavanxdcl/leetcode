class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split(' ')
        ans=""
        x=0
        for i in range(k):
            ans=ans+s[i]+" "

        return ans[:len(ans)-1]
        