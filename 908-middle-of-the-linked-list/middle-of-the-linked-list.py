# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        ll=[]
        t=head
        while(t):
            ll.append(t.val)
            t=t.next
        n=len(ll)
        middle=n//2
        t2=head
        c=0
        while(t2):
            if c==middle:
                return t2
            t2=t2.next
            c+=1
        
        