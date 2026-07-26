# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        copy=head
        ans=head
        while(head!=None):
            x.append(head.val)
            head=head.next
        x.sort()
        i=0
        while(copy!=None):
            copy.val=x[i]
            i=i+1
            copy=copy.next
        return ans