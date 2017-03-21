class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
            
        count = n-2
        fill = [True] * n
        fill[0], fill[1] = False, False
        for i in range(2, int(n**0.5 +1 )):
            if fill[i]:
                for j in range(i*i, n, i):
                    if fill[j]:
                        count -= 1
                        fill[j] = False
           
        return count
        
        
        
