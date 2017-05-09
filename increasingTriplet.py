class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        n_min = nums[0]
        middle = float("inf")
        for i in range(1, len(nums)):
            if nums[i] > n_min:
                if nums[i] > middle:
                    return True
                elif nums[i] < middle:
                    middle = nums[i]
            elif nums[i] < n_min:
                n_min = nums[i]
        
        return False
        
        
        
