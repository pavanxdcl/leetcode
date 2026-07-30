class MinStack:

    def __init__(self):
        self.a=[]
        self.m=[]
    def push(self, value: int) -> None:
        self.a.append(value)
        if(len(self.a)==1):
            self.m.append(self.a[0])        
        elif(self.m[-1]>value):
            self.m.append(value)
        else:
            self.m.append(self.m[-1])
    def pop(self) -> None:
        self.a.pop()
        self.m.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()