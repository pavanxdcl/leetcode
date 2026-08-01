class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h={}
        for i in arr:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        
        return len(list(set(arr)))==len(list(set(h.values())))
        