class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
            
        if t == 0:
            maps  = {}
            for i in range(len(nums)):
                if nums[i] in maps and i-maps[nums[i]] <= k:
                    return True
                maps[nums[i]] = i
            
            return False
            
        maps  = {}
        for i in range(len(nums)):
            keys = nums[i]/(t+1)
            for ky in (keys, keys+1, keys-1):
                if ky in maps and i-maps[ky][0] <= k and abs(nums[i] - maps[ky][1]) <= t:
                    return True
            maps[keys] = (i, nums[i])
            
            
        return False
        
        
        
