class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or nums[0] > nums[1]:
            return 0
            
        left = 1
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if nums[left] < nums[mid] and nums[mid-1] < nums[mid]:
                left = mid
            else:
                right = mid
        
        return (left+right)/2
        
        
        
        
        
