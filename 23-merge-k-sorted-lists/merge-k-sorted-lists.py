# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=[]
        for i in lists:
            x=i
            while(x!=None):
                n.append(x.val)
                x=x.next
        n.sort()

        if(0==len(n) and len(lists)!=0):
            return None
        elif(len(n)==0):
            return None

        ans=None
        head=None
        for i in n:
            temp=ListNode(i)
            if ans==None:
                ans=temp
                head=temp
            else:
                head.next=temp
                head=head.next
        return ans