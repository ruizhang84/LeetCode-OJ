# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        plusOne_recur(dummy)
        if dummy.val == 0:
            return dummy.next
        return dummy
    
def plusOne_recur(head):
    if head is None:
        return 1
    if plusOne_recur(head.next):
        temp = head.val + 1
        head.val = temp%10      
        return temp > 9
    
    
