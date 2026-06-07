# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find mid
        slow,fast = head,head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        print(slow.val)
        
        sh = slow.next
        slow.next = None
        prev = None

        while sh:
            t = sh.next
            sh.next = prev
            prev = sh
            sh = t
        
        f,sh = head,prev
        while sh:
            t1,t2 = f.next,sh.next
            f.next = sh
            sh.next = t1
            f,sh = t1,t2
        


        

        
        
        