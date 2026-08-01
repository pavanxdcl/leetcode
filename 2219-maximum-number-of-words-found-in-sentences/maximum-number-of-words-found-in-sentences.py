class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        x=0
        for i in s:
            x=max(x,len(i.split(' ')))
        return x
        