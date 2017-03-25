class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        
        if t == 0:
            maps  = {}
            for i in range(len(nums)):
                if nums[i] in maps and i-maps[nums[i]] <= k:
                    return True
                maps[nums[i]] = i
            return False
            
        for j in range(1, k+1):
            for i in range(len(nums)-j):
                if abs(nums[i]-nums[i+j]) <= t:
                    return True
        return False
        
        
        
