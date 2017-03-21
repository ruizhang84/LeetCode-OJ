class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == m:
            return n
            
        if len(bin(n)) != len(bin(m)):
            return 0
        
        t, k = 1, m
        while m > 0:
            if m & 1 == 1 and m < n:
                k -= t
            t <<= 1
            m >>= 1
            n >>= 1
        
        return k
        
        
        
        
        
