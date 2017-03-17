class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        elif len(nums) == 1:
            return nums[0]
        
        left, right =0, len(nums)-1
        while right - left > 1:
            mid = (left + right)/2
            if nums[mid] >= nums[right]:
                left = mid
            else:
                right = mid


                
            
        return min(nums[left], nums[right])
        
        
        
     
     
