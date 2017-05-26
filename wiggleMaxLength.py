class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        deLine = inLine = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inLine = deLine+1
            elif nums[i] < nums[i-1]:
                deLine =  inLine+1
                
        return max(deLine, inLine)    
        
        
