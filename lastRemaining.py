class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        index = 1
        length = []

        while n > 1:
            n = n >> 1
            length.append(n)
        
        #length = length[::-1]    
        
        
        for i in range(1, len(length)+1):
            index = (length[-i] - index +1)*2
        return index
        
        
        
