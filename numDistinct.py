class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0
        
        dp = [0 for i in range(len(s))]
        
        #t_0
        if t[0] == s[0]:
            dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == t[0]:
                dp[i] =  1

        #t_i
        old = dp[:]
        for i in range(1, len(t)):
            dp, old = old, dp
            dp[0] = 0
            cur = old[0]
            for j in range(1, len(s)):
                if s[j] == t[i]:
                    #thi is sum(old[:j])
                    dp[j] = cur 
                else:
                    dp[j] = 0
                cur += old[j]
        return sum(dp)
        
                
