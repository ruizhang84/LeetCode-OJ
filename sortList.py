class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = head
        arr = []
        while root:
            arr.append(root.val)
            root = root.next
        arr.sort()
        
        root = head
        for i in range(len(arr)):
            root.val = arr[i]
            root = root.next
            
        return head
