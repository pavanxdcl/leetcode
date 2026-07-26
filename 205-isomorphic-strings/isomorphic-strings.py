class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sh={}
        th={}
        i=0
        for i in range(len(s)):
            if s[i] in sh.keys():
                if sh[s[i]]!=t[i]:
                    return False
            elif t[i] in th.keys():
                if th[t[i]]!=s[i]:
                    return False
            else:
                sh[s[i]]=t[i]
                th[t[i]]=s[i]
            i=i+1
        return True