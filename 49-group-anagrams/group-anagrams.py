class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for j in strs:
            x=j
            i=list(x)
            i.sort()
            i=str(i)
            if i in h.keys():
                h[i].append(x)
            else:
                t=[]
                h[i]=t
                h[i].append(x)
        l=[]
        for i in h.keys():
            l.append(h[i])
        return l