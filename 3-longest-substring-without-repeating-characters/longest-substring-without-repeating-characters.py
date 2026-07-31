class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=""
        full=0
        for j in s:
            if j not in temp:
                temp=temp+j
            else:
                full=max(len(temp),full)
                i=0
                while(temp[i]!=j):
                    i=i+1
                i=i+1
                temp=temp[i:]
                temp=temp+j
        return max(full,len(temp))
        