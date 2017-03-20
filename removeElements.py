# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head and head.val == val:
            head = head.next
            
        root = head
        while head:
            #temp = head.next
            #while temp and temp.val == val:
            #    temp = temp.next
            #head.next = temp
            #head = temp
            
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
        
        return root
        
        
        
