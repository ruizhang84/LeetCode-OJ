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
            
        maps = {}
        for i in range(len(nums)):
            if i-k > 0:
                del maps[ nums[i-k-1]/t ]
            temp = nums[i]/t
            for j in (temp, temp-1, temp+1):
                if j in maps and abs(maps[j] - nums[i]) <= t:
                    return True
            maps[temp] = nums[i]
            
        return False
        
        
        
