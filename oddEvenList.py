# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
            
        root = head    
        old = head
        even = head.next
        
        dummy = head.next

        while head and dummy:
            head.next = dummy.next
            old = head
            head = head.next
            if head:
                old = head
                dummy.next = head.next
                dummy = dummy.next
        old.next = even
        
        return root
        
