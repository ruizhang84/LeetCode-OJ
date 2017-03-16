class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        root = ListNode(0)
        root.next = head
        temp = head.next
        head.next = None
        head = temp
        
        while head:
            back = root
            front = root.next
            while front:
                if head.val > front.val:
                    back = front
                    front = front.next
                else:
                    break
            
            temp = head.next
            head.next = back.next
            back.next = head
            head = temp
            
        return root.next   
