class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minq = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)
        if len(self.minq) == 0 or self.minq[-1] >= x:
            self.minq.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.minq[-1] == self.arr.pop():
            self.minq.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minq[-1]
        
        
        
        
