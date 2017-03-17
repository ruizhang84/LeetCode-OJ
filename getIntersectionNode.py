class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
            
        tempA, tempB = headA, headB
        while tempA != None and tempB != None:
            tempA, tempB = tempA.next, tempB.next
            
        while tempA != None:
            headA, tempA = headA.next, tempA.next
            if headA == None:
                return None
        while tempB != None:
            headB, tempB = headB.next, tempB.next
            if headB == None:
                return None
                
        while headA != None:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
    
        return None
        
        
        
        
