class Solution:
    def calPoints(self, o: List[str]) -> int:
        s=[]
        score=0
        for i in o:
            if i=="C":
                s.pop()
            elif i=="D":
                ans=(s[-1]*2)
                s.append(ans)
            elif i=="+":
                ans=(s[-1]+s[-2])
                s.append(ans)
            else:
                s.append(int(i))
        # print(s)
        for i in s:
            score=score+int(i)
        return score