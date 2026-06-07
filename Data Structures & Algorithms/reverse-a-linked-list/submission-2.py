# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        s = []

        while head is not None:
            s.append(head)
            head = head.next

        if len(s)==0:
            return None
        nh = s.pop()
        t = nh
        while len(s)>0:
            a = s.pop()
            t.next = a
            t = a

        t.next = None
            

        return nh

        