class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        base = 0
        for i in range(len(A)):
            base += i*A[i]
            
        sums = sum(A)
        maxV = base
        
        for i in range(len(A)):
            base = base - (len(A)*A[len(A)-i-1]-sums)
            if base > maxV:
                maxV = base
                
        return maxV 
        
        
