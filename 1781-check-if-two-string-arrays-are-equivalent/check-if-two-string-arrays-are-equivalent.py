class Solution:
    def arrayStringsAreEqual(self, w: List[str], ww: List[str]) -> bool:
        x=""
        for i in w:
            x=x+i
        
        y=""
        for i in ww:
            y=y+i
        
        return x==y

        