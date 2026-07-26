class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal):
            return False
        s=s+s
        for i in range(0,len(s)-len(goal)):
            if(s[i:i+len(goal)]==goal):
                return True
        return False
        