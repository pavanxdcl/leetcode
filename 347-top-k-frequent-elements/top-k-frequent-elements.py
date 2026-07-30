class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        h={}
        ans=[]
        for i in a:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
            
        v=list(h.values())
        while(len(ans)!=k and len(v)!=0):
            curr=max(v)
            v.pop(v.index(curr))
            for i in h.keys():
                if h[i]==curr:
                    ans.append(i)
                    h.pop(i)
                    break
        return ans