# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        if(not(h1) and not(h2)):
            return None
        h3=None
        save=None
        curr=None

        while(h1 and h2):
            if(h1.val < h2.val):
                curr=h1
                h1=h1.next
                curr.next=None
                if(h3==None):
                    h3=curr
                    save=h3
                else:
                    h3.next=curr
                    h3=h3.next
            else:
                curr=h2
                h2=h2.next
                curr.next=None
                if(h3==None):
                    h3=curr
                    save=h3
                else:
                    h3.next=curr
                    h3=h3.next
        
        if(h3==None and h1):
            return h1
        if(h3==None and h2):
            return h2
        if(h1 != None):
            h3.next=h1  
        else:
            h3.next=h2
            
        return save

        