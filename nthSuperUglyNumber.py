class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        point = [ 0 for i in range(len(primes))]
        curr  = [ 1 ]
        
        count = 0
        while True:
            temp = float("inf")

            for i in range(len(primes)):
                if temp > curr[point[i]]*primes[i]:
                    temp = curr[point[i]]*primes[i]

            for i in range(len(primes)):
                if curr[point[i]]*primes[i] == temp:
                    point[i] += 1
                    

            curr.append(temp)
            count += 1
            
            if count == n-1:
                return temp
        
        
        
        
