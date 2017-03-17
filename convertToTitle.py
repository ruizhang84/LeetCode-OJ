class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans, n = '', n-1
        #maps = [s for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        while n >= 0:
            #ans = maps[n%26] + ans
            ans = chr(n%26+65) + ans
            n = n/26-1
            
        return ans 
        
        
