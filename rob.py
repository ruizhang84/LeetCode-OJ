class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return sum(nums)
        if len(nums) < 4:
            return max(nums)
        
        
        prevs = 0
        prevt = 0
        cur_s = nums[0]
        cur_t = 0
        
        for i in range(1, len(nums)-1):
            temp = cur_s
            cur_s = max(cur_s, prevs + nums[i])
            prevs = max(temp, prevs)
            
            
            temp = cur_t
            cur_t = max(cur_t, prevt + nums[i])
            prevt = max(temp, prevt)
        
        cur_t = max(cur_t, prevt + nums[-1])  
            
        return max(max(prevs, prevt), max(cur_t, cur_s))
        
        
        
