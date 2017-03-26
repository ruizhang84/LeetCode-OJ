class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.store = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue) > 1:
            self.store.append( self.queue.pop(0) )
        temp = self.queue.pop()
        self.queue, self.store = self.store, self.queue
        return temp
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        temp = None
        while self.queue:
            temp = self.queue.pop(0)
            self.store.append(temp)
            
        self.queue, self.store = self.store, self.queue
        
        return temp
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


