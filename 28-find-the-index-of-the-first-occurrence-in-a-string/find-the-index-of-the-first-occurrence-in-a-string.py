class Solution:
    def strStr(self, h: str, n: str) -> int:
        h=h.replace(n,'+')
        h=list(h)
        if '+' in h:
            return h.index('+')
        return -1
        