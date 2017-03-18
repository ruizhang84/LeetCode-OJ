class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator*denominator >= 0:
            ans = str(numerator/denominator)
            rest = numerator%denominator
        else:
            ans = '-'+ str(-numerator/denominator)
            rest = -numerator%denominator
            
        if rest == 0:
            return ans
            
        visited = {}
        decimal  = ''
        start = 0
        while rest != 0:
            if rest in visited:
                return ans + '.' + decimal[:visited[rest]] + '(' + decimal[visited[rest]:] +')'
            visited[rest] = start
            decimal += str(rest*10/denominator)
            rest = rest*10%denominator
            start += 1

        return ans + '.' + decimal
        
        
        
        
