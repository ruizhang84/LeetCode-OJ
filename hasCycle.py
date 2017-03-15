class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        car1 = car2 = head
        step = 1
        
        while True:
            for i in range(step):
                car1 = car1.next
                if car1 == None:
                    return False
                if car1 == car2:
                    return True
                
            for i in range(step):
                if car1 == car2:
                    return True
                car2 = car2.next

            step <<= 1
        
