class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0 for i in range(target+1)]
        for i in nums:
            if i <= target:
                dp[i] = 1
            
        for i in range(target+1):
            for j in nums:
                if i-j > 0:
                    dp[i] += dp[i-j]
                else:
                    break
              
        return dp[target]
        
        
        
