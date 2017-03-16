class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return 
        
        car1 = head
        car2 = head.next
        while car2:
            car2 = car2.next
            if car2:
                car1 = car1.next
                car2 = car2.next
                
        front = car1.next
        back = car1
        car1.next = None
        while front:
            temp = front.next
            front.next = back
            back = front
            front = temp
        
        root = head
        while root:
            temp = root.next
            temp2 = back.next
            root.next = back
            #root = temp
            back.next = root = temp
            back = temp2
        
        
