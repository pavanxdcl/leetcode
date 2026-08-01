# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        ans=[]
        while(head):
            ans.append(head.val)
            head=head.next
        ans=ans[::-1]
        head=x
        for i in ans:
            x.val=i
            x=x.next
        return head

        