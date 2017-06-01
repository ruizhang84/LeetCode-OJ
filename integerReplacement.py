class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 1:

            if n % 2 == 0:
                n = n >> 1
                total += 1
            elif (n+1) % 4 == 0 and n != 3:
                n = (n+1)/2
                total += 2
            else:
                n = (n-1)/2
                total += 2
                
        return total
        
        
        
