# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return None
        
        slow=head
        fast=head

        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None

        s2=head
        while(s2!=slow):
            s2=s2.next
            slow=slow.next
        return slow